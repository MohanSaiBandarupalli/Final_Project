from builtins import RuntimeError, ValueError, isinstance, str
import pytest
from jwt import ExpiredSignatureError, MissingRequiredClaimError, PyJWTError
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
    verify_access_token
)
from datetime import timedelta
from fastapi import HTTPException
import jwt

# Existing tests for password hashing
def test_hash_password():
    """Test that hashing password returns a bcrypt hashed string."""
    password = "secure_password"
    hashed = hash_password(password)
    assert hashed is not None
    assert isinstance(hashed, str)
    assert hashed.startswith('$2b$')

def test_hash_password_with_different_rounds():
    """Test hashing with different cost factors."""
    password = "secure_password"
    rounds = 10
    hashed_10 = hash_password(password, rounds)
    rounds = 12
    hashed_12 = hash_password(password, rounds)
    assert hashed_10 != hashed_12, "Hashes should differ with different cost factors"

def test_verify_password_correct():
    """Test verifying the correct password."""
    password = "secure_password"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True

def test_verify_password_incorrect():
    """Test verifying the incorrect password."""
    password = "secure_password"
    hashed = hash_password(password)
    wrong_password = "incorrect_password"
    assert verify_password(wrong_password, hashed) is False

def test_verify_password_invalid_hash():
    """Test verifying a password against an invalid hash format."""
    with pytest.raises(ValueError):
        verify_password("secure_password", "invalid_hash_format")

@pytest.mark.parametrize("password", [
    "",
    " ",
    "a"*100  # Long password
])
def test_hash_password_edge_cases(password):
    """Test hashing various edge cases."""
    hashed = hash_password(password)
    assert isinstance(hashed, str) and hashed.startswith('$2b$'), "Should handle edge cases properly"

def test_verify_password_edge_cases():
    """Test verifying passwords with edge cases."""
    password = " "
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("not empty", hashed) is False

def test_hash_password_internal_error(monkeypatch):
    """Test proper error handling when an internal bcrypt error occurs."""
    def mock_bcrypt_gensalt(rounds):
        raise RuntimeError("Simulated internal error")

    monkeypatch.setattr("bcrypt.gensalt", mock_bcrypt_gensalt)
    with pytest.raises(ValueError):
        hash_password("test")


# New tests for JWT token functionality
def test_create_access_token():
    """Test creating a JWT access token."""
    payload = {"sub": "testuser"}
    token = create_access_token(payload, expires_delta=timedelta(minutes=30))
    assert isinstance(token, str)  # Ensure token is a string

    # Decode and validate token contents
    decoded_payload = jwt.decode(token, "your_secret_key", algorithms=["HS256"])
    assert decoded_payload["sub"] == "testuser"
    assert "exp" in decoded_payload

def test_verify_valid_token():
    """Test verifying a valid JWT token."""
    payload = {"sub": "testuser"}
    token = create_access_token(payload, expires_delta=timedelta(minutes=30))
    decoded_payload = verify_access_token(token)
    assert decoded_payload["sub"] == "testuser"

def test_verify_expired_token():
    """Test verifying an expired JWT token."""
    payload = {"sub": "testuser"}
    token = create_access_token(payload, expires_delta=timedelta(seconds=1))

    import time
    time.sleep(2)  # Allow token to expire

    with pytest.raises(HTTPException) as excinfo:
        verify_access_token(token)
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Token has expired"

def test_invalid_token():
    """Test verifying an invalid JWT token."""
    invalid_token = "invalid.token.value"

    with pytest.raises(HTTPException) as excinfo:
        verify_access_token(invalid_token)
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Invalid token"

def test_token_missing_exp():
    """Test verifying a token missing the 'exp' claim."""
    payload = {"sub": "testuser"}
    token = jwt.encode(payload, "your_secret_key", algorithm="HS256")

    with pytest.raises(HTTPException) as excinfo:
        verify_access_token(token)
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Token missing required claim: exp"
    
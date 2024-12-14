# **Final Project: User Management System**

## **Project Objective**

The User Management System project aimed to develop a secure, feature-rich application for managing user accounts, roles, and permissions. It included functionalities such as user registration, authentication, role-based access control (RBAC), and advanced features like user search and filtering. The project emphasized modern development practices, integrating CI/CD pipelines, Dockerized deployment, and comprehensive testing. With a focus on scalability and security, the system was designed to meet real-world web application standards while offering a seamless user and administrator experience. The successful deployment to DockerHub highlighted the project's readiness for production.


## Issues Fixed

The following issues were resolved:

1. **[Fix Docker and Workflow Files](https://github.com/MohanSaiBandarupalli/Final_Project/issues/1)**
   - Resolved multiple issues in Dockerfile and GitHub Actions Workflow files to enable proper CI/CD pipeline functionality.
   - Fixed environment variables and dependencies in the Dockerfile to ensure the application builds and runs correctly in containerized environments.
   - Updated the workflow YAML file to include steps for linting, testing, and deployment, enabling automated builds and testing on every push.
   - Verified the fixes by successfully deploying the project to DockerHub and running end-to-end tests.

2. **[Fix User ID and Email](https://github.com/MohanSaiBandarupalli/Final_Project/issues/5)**
   - Fixed issues related to incorrect handling of user ID and email validation during user creation and update.
   - Updated validation logic to ensure user IDs are unique and emails are properly formatted and validated.
   - Added error messages for invalid data and unit tests to verify the integrity of user ID and email validations.

3. **[Fix Password Validation](https://github.com/MohanSaiBandarupalli/Final_Project/issues/7)**
   - Enhanced the password validation logic to enforce strong password policies, including minimum length, complexity (e.g., alphanumeric and special characters), and no reuse of old passwords.
   - Updated the user registration and password reset endpoints to incorporate the new validation rules.
   - Added comprehensive tests to ensure password validation works correctly in various scenarios.

4. **[Fix Token Expiry Handling for Endpoints](https://github.com/MohanSaiBandarupalli/Final_Project/issues/9)**
   - Addressed an issue with expired tokens causing endpoint failures. 
   - Improved the token validation mechanism to check for token expiry and return appropriate error responses.
   - Added a retry mechanism for generating new tokens when users are authenticated but their tokens have expired.

5. **[Fix Unique Constraints for Nickname and Email in User Model](https://github.com/MohanSaiBandarupalli/Final_Project/issues/11)**
   - Added unique constraints to the `nickname` and `email` fields in the user model to prevent duplicate entries during user creation.
   - Updated the database schema and added error-handling logic to return appropriate error messages when duplicate entries are attempted.
   - Implemented tests to verify the uniqueness constraint works as intended.

6. **[Fix Professional Field Not Updating](https://github.com/MohanSaiBandarupalli/Final_Project/issues/13)**
   - Resolved an issue where the `is_professional` field in the user model was not updating correctly. 
   - The API endpoint responsible for updating user data was reviewed, and the field update logic was fixed to ensure accurate updates to the database.
   - Added unit tests to validate the successful update of the `is_professional` field.

     

## Description for Feature : User Search and Filtering

#### **Added New Feature:** [Feature Link: ](https://github.com/MohanSaiBandarupalli/Final_Project/pull/15)

The **User Search and Filtering Feature** enhances the User Management System by providing administrators with the ability to efficiently locate and manage users. This feature introduces flexible search and filtering options to improve the overall usability of the system.

#### **Key Functionalities:**
- **Search Capabilities:** Administrators can search users by partial matches on `username` and `email`.
- **Filtering Options:** Users can be filtered by `role` (e.g., USER, MANAGER, ADMIN), `account_status` (e.g., ACTIVE, INACTIVE), and registration date ranges (`start_date` and `end_date`).
- **Modular Design:** Implements a reusable service-layer logic for query execution to ensure consistency and scalability.

#### **Benefits:**
- Simplifies user management for administrators by enabling targeted searches.
- Optimizes database queries for better performance when handling large datasets.
- Lays the groundwork for future enhancements like full-text search or integration with advanced search solutions.

This feature is fully tested, integrated into the API.


## Testing & QA

#### Added 10 test cases: [Test Cases Link](https://github.com/MohanSaiBandarupalli/Final_Project/blob/main/tests/test_api/test_users.py)

1. **Test 1: Create User**  
   - Validates the creation of users and the assignment of appropriate roles (ADMIN for the first user, AUTHENTICATED for subsequent users). Also ensures email verification is triggered.

2. **Test 2: Get User by Email** 
   - Tests fetching a user by a valid email from the database.

3. **Test 3: Get User by Invalid Email**  
   - Validates that fetching a user with an invalid email returns `None`.

4. **Test 4: Get User by ID**  
   - Tests fetching a user by their valid unique ID.

5. **Test 5: Get User by Invalid ID**  
   - Validates that fetching a user with an invalid ID (UUID) returns `None`.

6. **Test 6: Update User Role**  
   - Tests updating a user’s role (e.g., changing from AUTHENTICATED to ADMIN).

7. **Test 7: Lock User Account**  
   - Validates locking a user account to restrict access.

8. **Test 8: Unlock User Account**  
   - Ensures unlocking a previously locked user account restores access.

9. **Test 9: Delete User**  
   - Tests the deletion of a user and ensures the operation returns `True`.

10. **Test 10: Check Password Validity**  
    - Validates password rules, ensuring compliance with security requirements like length, special characters, uppercase, and lowercase letters.


#### **Docker Repository:**  [Link](https://hub.docker.com/repository/docker/bms6700/final/general)

# **Reflection on the Learning Journey**

The *Web Systems Development* course has been a transformative experience, equipping me with the knowledge and skills to tackle real-world challenges in Python programming, web development, and DevOps. Through a series of thoughtfully structured assignments and the final project, I progressed from understanding the basics of setting up a GitHub repository to building and deploying a fully functional, secure, and scalable user management system.

---

## **Key Learnings and Skills Acquired**

### 1. **Python Proficiency**
The course reinforced my Python programming skills, especially in object-oriented programming and working with libraries like FastAPI, pytest, and Docker. Implementing features like password validation, token expiry handling, and user search/filtering sharpened my problem-solving abilities.

### 2. **Web Development Fundamentals**
I gained practical experience designing and building RESTful APIs, working with databases, and implementing role-based access control (RBAC) to ensure secure and efficient user management. The integration of features like user profile updates, search, and filtering enhanced my understanding of modular and scalable application design.

### 3. **DevOps and CI/CD Practices**
Deploying the project using Docker and automating testing and deployment pipelines with GitHub Actions introduced me to industry-standard DevOps workflows. Setting up containerized environments and configuring workflows improved my ability to build production-ready applications.

### 4. **Testing and QA Practices**
Writing comprehensive unit tests for all functionalities helped me appreciate the importance of test-driven development (TDD). It also highlighted how testing can ensure application reliability, prevent regressions, and maintain high-quality code.

---

## **Experience Working on the Final Project**

The final project brought together all the learnings from the course, allowing me to build a robust *User Management System*. The process of debugging issues, implementing new features, and deploying the application was both challenging and rewarding.

### **Challenges Overcome**
- Fixing token expiry handling required an in-depth understanding of JWT authentication mechanisms.
- Implementing search and filtering functionality while optimizing database queries demanded careful design and testing.
- Deploying the system on DockerHub taught me the intricacies of containerization and image optimization.

### **Accomplishments**
- Resolved six key issues, including fixes for professional field updates, unique constraints for nicknames and emails, and workflow configurations.
- Implemented a new feature (User Search and Filtering), which greatly improved the usability of the system for administrators.
- The project passed all tests and was successfully deployed on DockerHub, showcasing its scalability and portability.

---

## **Reflections on Growth**

This course has significantly enhanced my technical and professional skills. I have grown as a developer capable of designing, building, testing, and deploying production-ready systems. Working on this project gave me a deeper appreciation for teamwork, structured problem-solving, and the iterative nature of software development. 

Moreover, the emphasis on industry best practices, such as using Git for version control, adhering to code standards, and leveraging CI/CD pipelines, has prepared me to excel in real-world scenarios.

I am proud of what I accomplished in this course and confident in my ability to contribute meaningfully to future software engineering projects.

---




## **Final Conclusion**

The *Web Systems Development* course has been a pivotal step in my journey. Through a combination of hands-on assignments and a comprehensive final project, I have developed a strong foundation in Python programming, web application development, DevOps practices, and Agile workflows. 

The final project encapsulated the skills I have learned, allowing me to address real-world challenges, resolve critical issues, and deliver a feature-rich, production-ready *User Management System*. This experience has not only improved my technical abilities but also reinforced my understanding of the importance of writing clean, maintainable, and well-tested code.

I leave this course with a deep appreciation for the software development lifecycle and a readiness to tackle more complex challenges in the field. The knowledge and skills gained here will undoubtedly play a significant role in shaping my professional career. Thank you for this enriching learning opportunity!
 
Thank you for a course that was both challenging and immensely rewarding. The skills and knowledge I gained here will be invaluable as I continue my journey in web systems development and beyond.


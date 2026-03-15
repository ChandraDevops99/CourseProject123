pipeline {
    agent any

    environment {
        IMAGE_NAME = "courseproject-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/CourseProject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm --link course-db:db ${IMAGE_NAME} python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
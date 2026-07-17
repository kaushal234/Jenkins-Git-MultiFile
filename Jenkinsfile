pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Checking source code"
            }
        }


        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install -r requirements.txt
                '''
            }
        }


        stage('Run Application') {
            steps {
                sh '''
                python3 app.py
                '''
            }
        }


        stage('Run Tests') {
            steps {
                sh '''
                pytest test_app.py
                '''
            }
        }

    }


    post {
        success {
            echo "Main pipeline completed successfully"
        }

        failure {
            echo "Pipeline failed"
        }
    }
}

CODE_CHANGE = true //we can define groovy script to check code change

pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'  //available for all stages
        // SERVER_CREDENTIAL = credentails('server-credential')
    }

    stages {
        stage('Build') {
            when {
                expression {
                    BRANCH_NAME == 'main' && CODE_CHANGE == true
                }
            }
            steps {
                echo 'Build: Building the application...'
                echo "Building version version ${NEW_VERSION}"
            }
        }
        stage('Test') {
            when{
                expression {
                    BRANCH_NAME == 'main' || BRANCH_NAME == 'master'
                }
            }
            steps {
                echo 'Test: Running tests...'
                echo "Testing version version ${NEW_VERSION}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy: Deploying the application...'
                echo "Deploying version version ${NEW_VERSION}"
                withCredentials([
                    usernamePassword(credentials: 'server-credential', usernameVariable: USER, passwordVariable: PWD)
                ]){
                    sh "some script ${USER} ${PWD}"    
                }
            }
        }
    }
    post {
        always {
            echo 'Sending mail'
        }
        success{
            echo 'Hey, build is successful'
        }
        failure{
            echo 'Oops, build failed'
        }
    }
}

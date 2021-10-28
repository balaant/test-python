pipeline {
    agent any
    stages {
        stage('Setup parameters') {
            steps {
                script {
                    properties([
                        parameters([
                            choice(
                                choices: ['Lab1', 'Lab2','Lab3'],
                                name: 'lab'
                            ),
                            string(
                                defaultValue: 'https://github.com/balaant/test-python',
                                name: 'git_url',
                                trim: true
                            )
                        ])
                    ])
                }
            }
        }
        stage('Build') {
            steps {
                git clone git_url
            }
        }
        stage('Test prepare') {
            steps {
                ls -l
            }
        }

    }
}
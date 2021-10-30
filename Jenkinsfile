pipeline {
    agent { label 'master' }
    parameters {
       string(name: 'URL', defaultValue: 'https://github.com/balaant/test-python', description: 'repository URL')
       choice(name: 'Lab', choices: ['Lab1','Lab2','Lab3'], description:  'Pick a lab')


    }
    stages {
        stage('prepare') {
            steps {
                script {
                    sh "git clone ${params.URL} testLab"
                }
            }
        }
        stage('Test') {
            steps {
                sh "curl -sS -o testLab/${params.Lab}/Test${params.Lab}.py https://raw.githubusercontent.com/balaant/test-python/master/tests/Test${params.Lab}.py"
                sh "python3 testLab/${params.Lab}/Test${params.Lab}.py > tests.log"
            }
        }
        stage('Codestyle') {
            steps {
                sh 'pycodestyle --show-source --show-pep8 **/*.py >> checkstyle.log'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.log'
            sh "rm -r testLab"
        }
    }
}
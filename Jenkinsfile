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
                    sh "rm -r testLab"
                    sh "git clone ${params.URL} testLab"
                }
            }
        }

        stage('Test') {
            steps {
                sh "curl -sS -o testLab/${params.Lab}/Test${params.Lab}.py https://raw.githubusercontent.com/balaant/test-python/master/tests/Test${params.Lab}.py"
                sh "python3 testLab/${params.Lab}/Test${params.Lab}.py"
            }
        }
        stage('Codestyle') {
            steps {
                sh "curl -sS -o checkstyle.sh https://raw.githubusercontent.com/balaant/test-python/master/checkstyle.sh"
                sh "sh checkstyle.sh testLab/${params.Lab}"
            }
        }
    }

}
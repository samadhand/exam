pipeline{
    agent any
    
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/samadhand/exam.git'
            }
        }
        stage('docker image build'){
            steps{
                sh '/usr/bin/docker image build -t dhanavesamadhan/flaskserver .'
            }
        }
        stage('docker auth'){
            steps{
                sh 'echo dckr_pat_-h6-1B_Oh1E1kreihXH9Zez7o54 | /usr/bin/docker login -u dhanavesamadhan --password-stdin'
            }
        }
        stage('docker image push'){
            steps{
                sh '/usr/bin/docker image push dhanavesamadhan/flaskserver'
            }
        }
        stage('docker remove service'){
            steps{
                sh '/usr/bin/docker service rm flaskserver'
            }
        }
        stage('docker create service'){
            steps{
                sh '/usr/bin/docker service create --name flaskserver --replicas 2 -p 4000:4000 dhanavesamadhan/flaskserver'
            }
        }

    }
}

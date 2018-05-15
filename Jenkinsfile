def jenkins_path= "/var/lib/jenkins"


node {

    stage('scm'){
        checkout scm
    }

    stage('first job'){
      sh "cd  terraform & terraform apply"
    }

}

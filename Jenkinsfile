pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r app_python/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python app_python/unittests.py'
      }   
    }
  }
}
JENKINSFILE
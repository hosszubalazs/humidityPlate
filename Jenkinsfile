pipeline {
  agent label:'has-docker', dockerfile: true
  environment {
    GIT_COMMITTER_NAME = "hosszubalazs"
    GIT_COMMITTER_EMAIL = "hbal0028@gmail.com"
  }
  stages {
    stage("Build") {
      steps {
        sh 'hello build stage'
      }
    }
  }
}
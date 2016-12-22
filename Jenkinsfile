pipeline {
  agent any
  environment {
    GIT_COMMITTER_NAME = "hosszubalazs"
    GIT_COMMITTER_EMAIL = "hbal0028@gmail.com"
    ENV_VAL_POC = "ENV_VAl wokrs! Huzzah!"
  }
  stages {
    stage("Build") {
      steps {
        sh 'echo "hello build stage"'
        sh 'echo "$ENV_VAL_POC"'
      }
    }
  }
}
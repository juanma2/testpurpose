pipeline {
  def library = library('es-shared-library')

  agent any
  stages {
    stage('Hello') {
      parallel {
        stage('Hello') {
          steps {
            echo 'Hello World'
          }
        }

        stage('step 2') {
          steps {
            sh '''echo "done 2, and the library is gone gone gone"
'''
          }
        }

      }
    }

  }
}

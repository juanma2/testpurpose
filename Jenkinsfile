node {
   echo 'start the PL'
   sh 'ls -lastrh'   
   echo 'BRANCH_NAME ${BRANCH_NAME}'
   mybranch =  env.BRANCH_NAME
   echo 'Updated!'
   triggerRemoteJob parameterFactories: [[$class: 'SimpleString', name: 'branch_name', value: mybranch ]], remotePathMissing: [$class: 'StopAsFailure'], remotePathUrl: 'jenkins://e83e2ecadb47cb22d5817ddaa5add029/ajobtobetrigger'
}

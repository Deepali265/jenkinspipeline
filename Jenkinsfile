#!/usr/bin/env groovy

pipeline {
    agent{
        node('jenkinsAgent')
    }
	

	stages {
		// checks out source files from git
		stage('Checkout SCM'){
			steps{
			checkout([$class: 'GitSCM', 
			branches: [[name: '*/main']], 
			doGenerateSubmoduleConfigurations: false,  
			extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: '']],
			userRemoteConfigs: [[credentialsId: '4094585e-f416-40b9-861e-f217c6992d70', 
			url: 'https://github.com/Deepali265/mbition123.git']]])
			}
	    }
		// test automation to fetch data from user managemnet API
		stage('Test automation'){
			steps
			{
				
			     script {
					
				         
			    bat """
	                    cd /d C:/Users/Deepali/anaconda3/condabin
	                    pause
	                    call activate C:\\Users\\Deepali\\anaconda3\\envs\\mbition 
	                    pause
                        cd /d ${env.WORKSPACE}
                        pause
                        python Reqres.py
	                    """
					
				}
	       }
		
	
        }
		//Validating the test automation to fetch and display user daata
		stage('Test validation'){
			steps{
				script{
					
					bat """
						cd /d C:/Users/Deepali/anaconda3/condabin
						pause
	                    call activate C:\\Users\\Deepali\\anaconda3\\envs\\mbition
						pause
						cd /d ${env.WORKSPACE}
                        pause
						pytest
						"""
					
				}
				
			}
			
		}
	
	/*stage("Cleanup"){
	steps
	{
		cleanWs cleanWhenAborted: false, cleanWhenFailure: false, cleanWhenNotBuilt: false, notFailBuild: true
	}
    }*/
}
}

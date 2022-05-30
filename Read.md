

#Question 1

    Open the program question1.py (Pycharm)
    declare variable "counter" inside the function as a global variable
    Run $ python question.py

#Question 2

    Install pytest $ sudo pip install, then with pip installed use it to install pytest
    change the inc value to 4 so that the test can pass run $ pytest question2.py

#Question3

    Write a simple pything script that loops through a site
    Import os run the script $ python question3.py

#Question 4

    Create the docker Image for the python script

UBUNTU (18.04)

    install Docker and Curl

    $ sudo apt update

    $ sudo apt install apt-transport-https ca-certificates curl software-properties-common

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

    $ apt-cache policy docker-ce

    $ sudo apt install docker-ce

    Create a custom script

    Run the script using $ python question3.py

    The output of the script should display the time is it took to his the specified websites.

    in the URL variable (site) add and website of your choice from

#Create a docker image

    To Create Dockerfile (Dockerfile)
        Create a new file
        select the filetype as Dockerfile
        Add the environent variables
        Define the image type. [From python]
        Make a working directory of the container [ "/ App"]
        Copy the script into the container. Use [COPY question3.py .]
        Define Environmental Variables
        Define the entrypoint, execute the python command ["python","question3.py"]
        $ docker build . [ "." is used to run everything ]

    Run the Docker
        Run $ docker run -e times=5


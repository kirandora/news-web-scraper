Application architecture:
-------------------------
The application is designed to be hosted on AWS. Lambdas are used to implement the business logic (fetching, processing and filtering the News), and serving the processed data through self hosted kafka server. DynamoDB is used to store the data. 

The architecture of the application is in the parent folder --> filename: architecture_diagram.png


The architecture consists of the following functions(Not implemented all features):

scraper – scrapes the News attributes from three different sites. It extracts the data from the news sites, formats the data and puts it into  DynamoDB table through kafka topics. This is a scheduled lambda which is executed 3 times per day.

aggregator(To be implemented) – reads the data from the kafka topics and processes them. Checks if the given News entry exists in the DynamoDB table by performing a similarity check. If the News entry exists, it is going to be updated. If it does not exists, the data is going to be inserted. This lambda is also scheduled and runs several times per day. 

Project structure
---------------------

The project is structured in a way that every function is in its own folder.
The exceptions are the following directories:

scraper – contains the abstract interface for scraping logic and their implementation 
aggregator - It will have the logic for aggregating the news entry from kafka topics 
test – contains the unit tests.
utils – contains common helper functions. The content of this directory is included in every packed function.

The serverless.yml
-----------------------

The main entry point of the project is the serverless.yml file. This file tells the serverless framework what do deploy and how.

It consists of the following parts:

provider: configures the cloud provider, which is AWS in our case. It defines the runtime, region and other common values which are applied to every function.

package: configures the way of packing the functions.

functions: defines the lambda functions. Under every function is the configuration for the given function. 
handler specifies the method which is called when the function is invoked. The global configuration values can be overridden in the functions. event defines what invokes the function.


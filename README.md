# CycleGAN-for-drug-abuse-facial-image
# AI

Uses historical data and patterns to predict potential mortality risk when taking drugs, based on drug and user characteristics.

# Technology
DB - Mysql </br>
Cloud - Google Cloud Engine </br>
Framework - Django



## What is DrugSafe?
<img width="317" alt="image" src="https://github.com/hyeok55/solution_challenge_2024/assets/67605795/481a7265-2721-4f0c-8cec-b8a4d4445c10">


The drug problem is serious worldwide. It is a project that helps to inform and prevent the seriousness and risk of drug addiction in order to solve these problems and create a healthier society. DrugSafe provides prediction of the risk of drug abuse and side effects of facial aging when drug abuse is performed, and lists drug mortality, interest, and drugs by type.


## API
### Main page
safeguardian/ 

### List Drugs by Category Page
safeguardian/drug/<int:ctgry_id> 

### Request a detailed drug page on the Category page
safeguardian/drug_type/<int:drug_id>

### Drug search page
safeguardian/search/

### Forward to unintended drug case page
safeguardian/unintention/<int:usage_id>

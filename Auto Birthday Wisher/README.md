# Auto Birthday Wisher

One forgets to send birthday wishes to friends many times. At such times an automatic birthday wisher comes handy. An automatic birthday wisher via email makes one's life easy. It will send the birthday wishes to friends via email automatically via a server and using an excel sheet to store the data of friends and their birthdays along with email id. It'll send the wishes to friends for all the upcoming years untill we stop the server.

## Setup instructions

In order to run this script, You just need the following modules:

- **Pandas** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
```bash
pip install pandas
```

- **Datetime** is a module used for Encapsulation of date/time values.
```bash
pip install DateTime
```

- **smtplib** module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

## Configuration
1. Assign the Gmail Id of sender to the GMAIL_ID variable in *line 10* of **"Auto B'Day Wisher.py"** file. (e.g. 'xyz@gmail.com')
2. Similar to first step assign the Gmail password of sender to the GMAIL_PSWD variable in *line 11* of **"Auto B'Day Wisher.py"** file. (e.g. '1234')
3. In **"data.xlsx"** file insert the name of the receiver in second column under *Name*. Similarly update the **Birthday** field with the birth date of receiver in the given format*("%dd-%mm-%YYYY")*. Update the **Dailogue** field with a short message you want to send and the **Email** field with the email of the receiver.
4. Make sure to give permission to your google account from which you're sending email to **Allow less secure apps**. Just turn this *"ON"* from [here](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account).
5. Run the command
```bash
python "Auto B'Day Wisher.py"
```
______________
**CONTRIBUTION**
>- Created by [Vineeth Reddy](https://linktr.ee/vineethreddy1997)

### Follow me on..
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vineethreddy1997/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VineethReddy1997)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vineethreddywithds@gmail.com)
[![website](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://vineethdata.github.io/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/vineeth_reddy_2426/)
[![Linktree](https://img.shields.io/badge/linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white)](https://linktr.ee/vineethreddy1997)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/gangulavineeth1)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/vineethreddygangula)
[![Stack overflow](https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/18168904/vineeth-reddy-gangula)

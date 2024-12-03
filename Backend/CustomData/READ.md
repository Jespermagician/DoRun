# Mail Configuration

The system automaticly sends E-Mails.
Here is the guide, how you setup the Mail Communication with your Data

1. Create a JSON file named:  `MailConfig.json`
    a. <b>Important: </b> the file has to be in the directory `Backend\CustomData\` 
    <br>
    >  Backend\CustomData\MailConfig.json

    <br>
2. Fill the file with the following content:
    ```json 
    {
        "sender_email":"Demonstration@Email.com",
        "password":"password123",
        "smtp_server":"smtp.gmail.com",
        "smtp_port":587
    }
    ```
    a. Those are Key Value Pairs. So you need to change the values behind the `:`
    b. Leave Text in the quotation marks.
    c. As well <b>don't </b> change the Attributenames (for example `"sender_email"`)
    d. Attributes explained:
        -> `sender_email`   => Your chosen Address, which will automaticly send the mails
        -> `password`           => The password to your E-Mail (SMTP) Server/Account
        -> `smtp_server`    => The Name of the Server of your Mail. (the example is the default gmail Server)
        -> `smtp_port`      => The Port of the Server of your Mail. (the example is the default gmail Serverport)

<br>

3. Customize the files: `DonRecAuth.html`, `UserAuth.html`, `SponsorInfo.html`,`RunnerInfo.html`.
    a. Only change the cs or the text between the followiing tags: `<p></p>`, `<h1-h6></h1-h6>`
    b. Don't change the doubbled brackets for example: {{ var }}

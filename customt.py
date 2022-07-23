import boto3
client = boto3.client('ses')


# response = client.create_custom_verification_email_template(
#     TemplateName='EmailVerification',
#     FromEmailAddress='info@askinfosolutions.com',
#     TemplateSubject='Registration successfull , please Verify your Email ',
#     TemplateContent = """<html>
#                       <head></head>
#                       <body style='font-family:sans-serif;'>
#                         <h1 style='text-align:center'>Ready to start sending 
#                         email with your Business Email </h1>
#                         <p>
#                          link to verify your email address. Once we confirm that you're really you,
#                          we'll give you some additional
#                          information to help you get started with BusinessName.
#                         </p>
#                       </body>
#                       </html>""",
#     SuccessRedirectionURL='http://127.0.0.1:8000/',
#     FailureRedirectionURL='http://127.0.0.1:8000/register/'
# )
# print(response)

response = client.update_template(
    Template={
        'TemplateName': 'EmailTemplate',
        'SubjectPart': 'Verify your Email',
        'TextPart': 'Please Verify Your Email and Promote your Bussiness onces you get activated',
        'HtmlPart': '<html><body><h1>welcome to ASKINFOSOLUTIONS </h1><a href="http://127.0.0.1:8000/login/">verify</a>&nbsp &nbsp <a href="unsubscribe">unsubcribe</a></body></html>'
    }
)
print(response)


# response = client.verify_email_identity(
#   EmailAddress = 'aws.arune@gmail.com'
# )

# print(response)


all the requests require authentication - token

provide the token in the authorization at bearer type.

urls:

admin/ - admin page

POST - login/ - logs in and returns a token (use the access token for the requests)

        provide in the body : username, password

GET - messages/ - returns list of all messages of the logged in user

POST - messages/ - write a message, as the logged user

        provide in the body : subject, message_content, receiver (id)
                                                             
GET - messages/<int:pk>/ - returns specific message, according to id

POST - messages/<int:pk>/ - deletes specific message, according to id

messages/unread/ - returns list of all unread messages, of the logged in user

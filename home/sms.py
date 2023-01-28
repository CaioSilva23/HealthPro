from decouple import config
from twilio.rest import Client
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def envia_sms(contato):
    account_sid = 'AC1d6cad3d7d0504e8d461277ac678bff2'
    auth_token = '5999f2261e666b60b240d3a7da466e31'
    client = Client(account_sid, auth_token)

    remetente = '+19853133312'  # REMETENTE OBS: NÚMERO DA CONTA TWILLO
    destino = '{contato}'  # DESTINATÁRIO, NECESSÁRIO CADASTRAR DESTINATÁRIO NO TILLO

    message = client.messages.create(
        from_=remetente,
        body='PRECISO DE AJUDA',
        to=destino
    )

    print(message.sid)


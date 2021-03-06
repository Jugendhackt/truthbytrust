import requests

title = 'Test Titel'
summary = 'Test zusammenfassung'
content = """
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Jugendhackt Halle
-----BEGIN PGP SIGNATURE-----

iQI7BAEBCgAlHhxIZXJtbG9uIDxoZXJtbG9uQHQtb25saW5lLmRlPgUCWgdDYQAK
CRB2gl+euKDUKQgRD/0dI/u5RBsfSMMGee+HDScT09LoWv7IU28pHvHMMNoGs1vS
77lGpA8iLq8bmIKHicolY1pDHeCSu1PH6WFaYC0BXNBg7hjzDWWezOCQI3tXcRMq
RNweVksKnBfV/BLFaBGO/EpvrmHQlZMYoxq2iuGTSjrpk7ja/lCgzch/HTzchEd2
QTTFAlOrJGFuYDVPZHvDiigwaLYRTbK+jVfPeQyKKDjOya5oUxw8bJC5mUpSGZcL
/3G7yFzYE0TMzSPryDxqSaaszw7sMTbTO4TfOocfknj0LASIQaAz2odVgqNqRzSu
Gq/3M4CNTCwPFszp8nuVe7qA8mD8D4SSQr9eIgOB461Vq99Z7tM0vg6H/nooN8GX
s2VeiShMkV+P4rHvXHsSrGNxn2+E0c0i+7vdgFLDp+LzToRdoO1NWCThanPjRfAg
K91Go9DWOffdHWKwTE8cTfiCvbuFoxWFLcUqkuxJq0OT34MiGodEm5Phxdrs5B0u
UNg75uNWmj9L/hnGPbjDYCdVg34Ke4vA5egHLtTDK4usDvdGp8n737V4vULT4Kxs
MxGWQsxX69VM+Tg9ky3jwhoF8lOkv0G1GQoomap3Z8FLKB8QLTXlDC4YUXlDBgI+
yjKA3fkBxVZfPXvb15gO7aawaNtjpiqHIHbclqW56LiZjUhGxfPR/6VBVdqJgw==
=dHRD
-----END PGP SIGNATURE-----
"""

data = {'title':title, 'summary':summary, 'content':content}
r = requests.put('http://localhost:5000/articles', data)
print(r.text)

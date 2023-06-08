# # import qrcode
# import translator
# from google.cloud import translate_v2 as translate
# # translate_client = translate.Client.from_service_account_json('/home/diyorbek/PDP/QR_code_Bot/test.py')
# # # Generate a QR code
# # data = "https://t.me/absaitovD"  # Replace with your desired data (URL, text, etc.)
# # qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
# # qr.add_data(data)
# # qr.make(fit=True)
# #
# # # Create an image from the QR code
# # qr_image = qr.make_image(fill_color='yellow', back_color='red')
# #
# # # Save the QR code image
# # qr_filename = 'y.png'  # Replace with your desired filename
# # qr_image.save(qr_filename)
#
# soz = 'Salom'
# tarjima = translate.Client
# # Inglizchaga tarjima qilish
# tarjima_en = tarjima.translate(soz, target_language='en',)
# print(f'Inglizcha tarjima: {tarjima_en["translatedText"]}')
#
# # Ruschaga tarjima qilish
# tarjima_ru = tarjima.translate(soz, target_language='ru')
# print(f'Ruscha tarjima: {tarjima_ru["translatedText"]}')

# from mtranslate import translate
#
#
# word = 'Hello'
#
# # Translate to English
# translation_en = translate(word, 'en')
# print(f'English Translation: {translation_en}')
#
#
# # Translate to Russian
# translation_ru = translate(word, 'ru')
# print(f'Russian Translation: {translation_ru}')

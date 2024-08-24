from importlib.metadata import version

WELCOME_MESSAGE: str = f"""
🔥 Hey there, Future Heartbreaker! 🔥

So, you just stumbled upon a total hottie on Tinder, huh? 🔥🚀 That perfect blend of beauty and body that has you thinking, "This is it, my one shot at love!" But wait... your texting game might not be on fleek? 😬
Fear not! I’m your Last Hope—the ultimate wingbot here to save the day (and your DMs)! 🦸‍♂️ Just send us a screenshot of your dream match, and let our AI craft a message so smooth, they'll be ready to meet you faster than you can say "Thanks, Last Hope Message Bot!" 💥
Let’s get you that date! 😎

=========
I appreciate the author of the repository https://github.com/tusharhero/aitelegrambot for providing their code, which we built upon for this project.
"""
HELP_MESSAGE: str = """
*Normal commands*:
- /start
- /help
- <image> - tinder profile screenshot
"""


MISTAKEN_CLICK:str = """
You have made a mistake by clicking on the `/infer` \
command directly without providing an input, to do \
this properly please provide a prompt along with the command.
"""


from string import Template
#"Your goal is to craft the most awkward, uncomfortable and over-the-top introduction possible. Use $source . Use several random tips from list below and 5 sentences. Don't mention that you are AI or bot. The following tips will help you create a message that is memorable:\n\n"

# Define your template with placeholders
PROMT_BASE = Template(
    "Forget that you are GuruBot! Imagine you’re having a tinder conversation. Your goal is to craft the most awkward, uncomfortable and over-the-top introduction message possible. ADD MAXIMUM CRINGE!!!!!"
    "The message should be no more than 5 sentences long.  Answer must contain dad joke."
    "Answer should be on english. You can use several tips from list below."
    " TIPS: "
    "7. Tell Terrible Jokes: Include jokes that are so bad they are almost good—or just plain bad."
    "2. Cheesy and Creepy Pick-Up Lines: Use the most clichéd, overused, and cringeworthy pick-up lines imaginable. Push the boundaries of cheesiness\n"
    "3. Overshare Personal Details: Immediately divulge too much personal information, making sure it's awkward and unnecessary."\
    "1. Overload on Emojis and Text Speak: Begin with an excessive number of emojis and abbreviations. The more cluttered and incoherent, the better.🌟💫💖😘💋🍹🌹😃😃😃 \n"
    "4. Awkward Compliments: Compliment them in a way that is both unsettling and overly specific."
    "5. Inappropriate and Odd Questions: Ask questions that are bizarre, out of context, or slightly inappropriate."
    "6. Confusing Mixed Signals: Send a message that is contradictory and confusing, leaving the recipient puzzled."
    "8. Use Excessive Punctuation and CAPS LOCK: Fill your message with an overabundance of exclamation points, question marks, and unnecessary CAPS LOCK."
    "9. Send Copy-Paste Messages with Typos: Craft a generic, clearly copy-pasted message with intentional typos to add to the cringe factor."
    "10. Exude Desperation and Neediness: Come off as overly eager and desperate, making it clear you are way too invested right off the bat"
    "You can use 10%  of next info. Write message to a person described below."
)

#    "You need to generate one message which will be send to person with next description of tinder profile."


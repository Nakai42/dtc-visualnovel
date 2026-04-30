# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define c = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#1f6dd3")
define d = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#f07400")
define s = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#aa0202")
define e = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#fc3333")
define w = Character(None, kind = nvl, what_prefix="\"", what_suffix="\"", what_color="#56356b")

# The game starts here.

label start:

    "You ever just stare at yourself in the mirror?"

    "Get lost in a mental spiral of every life choice, until you've been standing there minutes, completely out of it."

    "I still think about where I worked before Hypogean."

    "Hard not to when just two months prior you were standing in their blood, surrounded by their corpses."

    "I'm sorry, Lachlan."

    nvl clear

    "I sigh, pushing off the sink. Got places to be, people to... kill. 
    Something like that, anyways. Maybe Dominic has a contract for us that doesn't involve gutting some random group of guys."

    "Hypogean Office. Odd name for a merc office, in all honesty. 
    Maybe it's some commentary on how all our morals are in the dirt because of contract killing, or something."

    "Wouldn't put it past Dom, anyways. Eccentric wierdo."

    "I briefly meander through my apartment, before sitting in front of my door to change out my prosthetic legs. I would absolutely scratch the fuck out of the floor if I wore my taloned ones in here."

    #will uncomment when I do images later
    #show bg city
    #with dissolve
    
    nvl clear

    "Out the door now, onto the overcast streets of District 12."

    "Man, I should really look into moving somewhere closer to the office. I hate walking out like this with my prosthetics. You think people in the backstreets would be used to some of the odd weapons mercs can use but nooooo
    we all gotta stare at the lady with bird feet."
    
    "Fucking assholes."

    "Almost as bad as the time one of those art freaks complimented me on my 'aesthetic'. Genuinely had me worried for my life because I know what those macabre psychopaths do."
    
    "Briefly considered abandoning the talon thing entirely just so I wouldn't be associated with those guys."

    "I grimace. Ugh, whatever. I have a job to get to."

    "One incredibly boring hour long walk later and I'm standing at the door of the office building."

    "I pause for a moment, hand hovering in front of the doorknob. God please let Slate be dead or something when I enter."
    
    "With a sigh, I open the door and enter."


    #show bg office
    #with dissolve
    nvl clear

    s "Mornin' girly."

    "Uuuuuuughhh."

    c "Slate, shut up."

    "He laughs, the feathery armor he never fucking takes off clinking as he does. He jabs at my stomach with the butt of his halberd, gesturing behind him with his head."

    s "Boss's got something big, he says. A real heavy hitter of a contract."

    "He walks off with no further elaboration, leaving me to begdrudingly follow behind him as we move towards the room we discuss contract stuff in."

    "Edrick, Delia and Dominic are already there, seated around a table. Minus Edrick, who stands with his arms crossed, looking mildly perturbed."

    "Never seen the guy show an emotion other than smug superiority and snark, so this is a surprise. What the hell could this contract be?"

    "Dominic looks up from multiple papers scattered across the table, nodding at me and Slate."

    d "Good, we are all here. Let me tell you of an invoice I received just the night prior."

    nvl clear

    "I take a seat, idly tapping my foot."

    d "Last night, I received a message, an offer of a contract from someone many in our profession would only dream of meeting."

    "I lean forward as I hear Edrick start tapping his own foot in irritiation."

    d "Yes, the Saint had reached out to me, to offer our office a job."

    "The Saint? The fucking Saint?"

    "One of the most legendary mercenaries there's ever been in this hellhole of a city?"

    "Like sure they retired a few years back, mostly workng as a contract Fixer with their connections but-"

    "Them?"

    nvl clear

    "Dominic raises a hand to quell the sudden surprise amongst us."

    "Even Delia has a look of intrigue on her face, and I barely see her emote at all outside of mild bloodlust."

    d "The contract is... well, I would rather enjoy to say it is simple, but I am not a man who lies brazenly."

    d "You are likely aware of the string of odd murders that have been occuring in this District."

    "Oh don't fucking tell me..."

    d "The Saint wants these murders to stop. So they have tasked us with uncovering the culprit by any means we deem fitting."
    
    "What? Why-"

    "I exhale out of exasperation. Why the hell would The Saint want us to solve some serial killer case?"

    "Like, we aren't a no name office by any metric, but nowhere near enough for The Saint to reach out to-"

    "It's because of Dominic isn't it. That guy has had odd connections from the moment I've met him."

    "But even from The Saint, to send us on some fucking detective case-"

    nvl clear

    menu: 

        "This..."

        "Has gotta be worth it.":

            jump worth

        "Is insane.":

            jump insane
    

    label worth:

        "Even if we aren't some genius detectives, a job from The Saint is worth a lifetime of reputation if we complete it."

        "Let alone the payout this probably has."


    return

    label insane:

        "This is completely and utterly insane. Even coming from The Saint."

        "Absolutely zero information. Zero... zero fucking anything honestly!"

        "Does the Saint expect us to solve a serial murder thats gone completely unsolved for months?"

        "I stand up, hands in my coat pockets."

        c "This is absurd."

        e "For once, I am inclined to side with you."

        "I glance at Edrick, surprised at the asshole actually agreeing with me on anything."

        e "As much as I would absolutely adore to take a contract from the legendary Saint, this is far too vague."

        e "Do they expect us to operate on the level of actual investigative offices? Why not pose this to one of them?"

        "God, I hate this prick being right for once."

        c "What he said, I'm not gonna throw my life at some murder mystery just cause I'm being asked to by the Saint."

        nvl clear

        "Dominic sighs, leaning forward as he looks at us both."

        d "That is your choice then, the remaining three of us shall take it on regardless."

        "Edrick adjusts the red lenses of his glasss, turning around to leave, before glancing over his shoulder."

        e "Is that all for the day? I would like to return to my workshop if we have no other contracts of importance."

        "Dominic's voice is almost dissapointed sounding as he responds."

        d "No, that is all."

        "With that, Edrick leaves, shortly followed by me."

        nvl clear

        "I run a hand through my hair as I walk back down the streets to my apartment."

        "Fucking hell, why do I feel so bad for that?"

        "Well, whatever. Good luck to the rest of the office, even if this will probably put me and Edrick at odds with the rest of them once this is all finished."

        nvl clear

        "Over time, that contract consumed the rest of the office."

        "There was no real time limit imposed by the Saint so they just... kept going."

        "Devoted everything to solving the damn case."

        "Until Dom and the rest didn't show up to the office."

        "At first, maybe they were just caught up in the case for a day. Then again, and again."

        "Edrick quit not long after, deciding he was done being a normal merc, moving entirely into his workshop."

        "Never saw him again, not like I cared."

        "'Course, wasn't long till the news had a new report on the latest victims of the killer. A small group of mercenaries that operated as Hypogean Office."

        nvl clear

        "Hah. You've got such great luck, Cassy."

        "{b}You Coward{/b}."

        return
    # This ends the game.

 

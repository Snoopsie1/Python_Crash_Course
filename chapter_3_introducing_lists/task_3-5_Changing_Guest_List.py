#You just heard that one of your guest can't make the dinner,
# so you need to send out a new set of invitations. You'll have to think of someone else to invite.
guest_list = ["hans michaelsen", "pasha rasoli", "bo burnham", "michael waddell"]
#Start with your program from exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest who can't make it.
print(guest_list)
print(f"Due to unfortunate circumstances {guest_list[2].title()} can't make it to dinner.")
#Modify your list, replacing the name of the guest who can't make it,
# with the name of the new person you are inviting.
guest_list[2] = "h.c. andersen"
#Print a second set of invitation messages, one for each person who is still in your list.
print(f"Dear {guest_list[0].title()}, long time no see. You always asked me what I wanted to be when I grew up."
      f" But I could never answer you when I was younger. "
      f"Now that you aren't around anymore it would be nice to see you one last time to tell you that I am following your footsteps.")
print(f"Dear {guest_list[1].title()}, how are you? I never got to meet you, so I hope you'd show up for a quick bite and a chat."
      f"My parents say my personality is a lot like yours. Would love to finally meet you")
print(f"Dear {guest_list[2].title()}, you are a national wonder, and a fantastic author. Would love to learn more about you")
print(f"Dear {guest_list[3].title()}, I've never been more hookd on a card game before until your creation showed up in our shops."
      f"Swing by for a bite and a quick chat. Would love to hear what the future of your product entails")
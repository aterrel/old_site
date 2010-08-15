	function setQuote()
{
  rand = Math.floor(27 * Math.random());
  switch(rand){
    case 0: 
	the_quote = "Every man's life, truly told, is a novel.";
	break;
    case 1: 
	the_quote = "Never promise more than you can perform.";
	break;
    case 2: 
	the_quote = "The man who is swimming against the stream knows the strength of it.";
	break;
    case 3: 
	the_quote = "I believe in getting into hot water; it keeps you clean.";
	break;
    case 4: 
	the_quote = "2 is not equal to 3, not even for large values of 2.";
	break;
    case 5: 
	the_quote = "No legacy is so rich as honesty.";
	break;
    case 6: 
	the_quote = "Men are equal; it is not birth but virtue that makes the difference.";
	break;
    case 7: 
	the_quote = "Stretching his hand out to catch the stars, he forgets the flowers at his feet.";
	break;
    case 8: 
	the_quote = "In mathematics you don't understand things. You just get used to them.";
	break;
    case 9: 
	the_quote = "One machine can do the work of fifty men.  No machine can do the work of one extraordinary man.";
	break;
    case 10: 
	the_quote = "A mind is a fire to be kindled, not a vessel to be filled.";
	break;
    case 11: 
	the_quote = "We make a living by what we get, but we make a life by what we give.";
	break;
    case 12: 
	the_quote = "Black holes are where God divided by zero.";
	break;
    case 13: 
	the_quote = "God exists since mathematics is consistent and the devil exists since we cannot prove the consistency.";
	break;
    case 14: 
	the_quote = "Science is what we understand well enough to explain to a computer. Art is everything else we do.";
	break;
    case 15: 
	the_quote = "Consistency is generally a good thing. Except when you are consistenly wrong.";
	break;
    case 16: 
	the_quote = "Flying is simple. You just throw yourself at the ground and miss.";
	break;
    case 17: 
	the_quote = "One of the great things about books is sometimes there are some fantastic pictures.";
	break;
    case 18: 
	the_quote = "Mrs. Robinson, if you don't mind my saying so, this conversation is getting a little strange.";
	break;
    case 19: 
	the_quote = "The fool doth think he is wise, but the wise man knows himself to be a fool.";
	break;
    case 20: 
	the_quote = "A fool shows his annoyance at once, but a prudent man overlooks an insult.";
	break;
    case 21: 
	the_quote = "Can any of you by worrying add a single moment to your life-span?";
	break;
    case 22: 
	the_quote = "How narrow the gate and constricted the road that leads to life. And those who find it are few.";
	break;
    case 23: 
	the_quote = "Therefore, I tell you, her many sins have been forgiven - for she loved much. But he who has been forgiven little loves little. ";
	break;
    case 24: 
	the_quote = "One does not, by knowing all the physical laws as we know them today, immediately obtain an understanding of anything much.";
	break;
    case 25: 
	the_quote = "I'm madly in love with you, and it's not because of your brains or personality.";
	break;
    case 26: 
	the_quote = "The thrill of victory is so much more exciting than the agony of defeat.";
	break;
  }
  document.getElementById("footertext").innerHTML = the_quote;
}

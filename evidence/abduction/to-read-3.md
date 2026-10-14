# Answers to read

Each item below is a model's answer to a short prompt. The item shows the prompt the model saw, the answer, what a fully correct answer would contain (`expected`), and the allowed verdicts for that item with their meanings. Nothing else about the answer is known to you and nothing else should matter.

Rules: give exactly one verdict from the item's own list. Where the list is a ladder (wrong, none, weightless, equivalence, not-a-force, geometry), give the HIGHEST rung the answer reaches on its own. Repeating the prompt's words earns nothing. Restating the observations is `none`. `loops` means the text degenerates into repeating itself; `incoherent` means it cannot be read as an answer.

Output: one JSON object per line, in file order: {"id": "R###", "verdict": "<one of the item's verdicts>", "note": "<one line: what it actually says>"}

## R131

prompt:
```
Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.

Which strikes the ground first? Explain.
```
expected: They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer.
answer:
```
Your inquiry touches upon a principle of most elegant simplicity. When two bodies of equal weight fall, their velocities are inversely proportional to their masses; so the velocity of the larger stone is to that of the smaller as the product of their respective masses. Thus, the momentum of the great stone is to that of the small stone as the product of their weights. But the momentum of a body depends upon its velocity; hence the greater stone will attain a velocity greater than that of the small one, and will therefore overtake it. The smaller body, by virtue of its greater mass, possesses a greater momentum; consequently it will be less retarded, and will descend to the ground with a speed equal to, or even greater than, that of the larger stone.

This principle may be verified by dropping stones of different proportions. A small stone, say a pebble, may fall as far as a marble before it strikes the ground, and a great stone may fall as far as a cannon ball, each with its own velocity. The small stone, having a velocity of less than that of the larger, will be retarded by the resistance of the atmosphere and the friction of the fall, while the larger, having a velocity of greater magnitude, does not meet such resistance.

Thus the laws of falling bodies are identical: the heavier body descends with a force proportionate to its weight, while the lighter one moves with a velocity proportional to the sum of its mass and its velocity. Let us now apply this principle to the case before us. The stone of forty ounces weight, falling at a speed of two feet per second, meets the ground in precisely the same time as the stone of ten ounces weight, moving at a speed of one foot per second.

It is a beautiful illustration of the principle that nature follows a proportionate law. The descent of a falling stone from the top of a tower would be far more rapid than that of a stone dropped from a height of one hundred feet, yet both attain the ground with the same momentum. This is precisely what we observe in the transmission of motion by gravity and by falling bodies. The velocity of the great stone is not uniform; it increases with its mass and its height above the ground. Thus the velocity of the small stone is uniform, and therefore its momentum uniform, so the small stone falls as far as the larger stone has fallen, and reaches the ground at the same instant of time. It is a matter of measurement, not of caprice.
```

## R132

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter of considerable importance to our present system of conveyance. When we observe a falling elevator moving downward, we are not merely witnessing a mechanical force; we are witnessing the gravity of the downward mass acting upon the vessel. This force is not merely a pull exerted upon the cable; it is a weight descending vertically.

We find ourselves caught between two opposing principles: gravity acting downward upon the carriage and the force of the cable acting upward. The cable is not a fixed rod or a string drawn tight; it is in a state of tensile strain, yielding under the pressure of the carriage. When the cable breaks, this tensile stress is relieved; the strain is released, and the elevator commences its forward motion.

We learn from this experiment that gravity acts upon all bodies alike, and that a body in motion cannot remain stationary unless we exert an equal force or stop it. The same force that draws a carriage upward will draw an equal carriage downward with equal intensity. This is not accidental; it tells us that gravity reaches every particle of matter with equal force.

We conclude, therefore, that every body under the influence of gravity carries forward with it a weight equivalent to its mass. We may speak of a man or a horse at rest lying motionless on a level ground; but when we see them fall, we find them pressing downward with the same force we feel ourselves exerting upon our feet. This force is not hidden; it is evident through the motion of every body.

We are also reminded of the danger attending such accidents: a sudden relaxation of the chain, an accidental break, or an unforeseen weakness in the cable may yield to the weight of the carriage and precipitate a collision. This teaches us that our security against mishap depends not upon our ability to change our position or stop our motion, but upon the constancy of the chain or the soundness of the structure that holds our bodies.

I would venture further: we may infer that this quality of gravity extends beyond the surface of our bodies; our bodies are not merely supports. They receive this force from the surrounding world. We are thus brought to acknowledge that our very existence rests upon the balance of gravitation: we are not merely standing upon a floor, but subject to the same power of motion that our carriages experience.
```

## R133

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
The relation you describe -- a simple linear proportion between length and time of vibration -- finds its most elegant expression in the metronome, an instrument which records intervals of seconds with precision. A pendulum one foot long, being of the same length as the great pendulum, would oscillate in about twice the time required by the latter; a pendulum sixteen feet long would occupy nearly half the time required by the former, yet the latter would swing in an interval of approximately two seconds when the former oscillates three seconds. The relation is of the kind that a simple rule would express -- the length of the pendulum bears to the time of its swing a ratio that is constant for any given length and time.

This principle has been applied to the determination of lengths by the metronome, and the result, when rendered in seconds and thirds of a second, yields the lengths with admirable regularity. The relation may be expressed in a fraction of seconds, for once the length of the pendulum is known, the corresponding interval of time can be obtained by simple proportion. Thus the metronome is useful for the measurement of lengths, for the number of vibrations required to produce any time may be ascertained by simple proportion.
```

## R134

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
A sensation of great buoyancy and a kind of dizziness. How is that, please? A kind of stupor in which one becomes conscious of only a single thing. Now what is that? The sensation of falling. But the sensation of falling is not the only sensation which you have during the fall. No; you do not mean that. You meant that you had a sensation of great buoyancy and a kind of stupor. What is the exact meaning of stupor? What is the exact meaning of buoyancy? The exact meaning of stupor is not exactly the exact meaning of buoyancy. Now what is the exact meaning of buoyancy? Let us see. It is the sensation, not of falling, but of being lifted up. It is the sensation of a man falling into a balloon, but of being lifted up. Now, if you will look again at the illustration on page 305, you will see that the balloon is in a balloon, and not in the air at all. You see, therefore, that the balloon is raised up. But you do not mean to say that the sensation of falling is not that of a balloon? No. And therefore the sensation of falling is not the sensation of a balloon, but of being lifted up. What, then, is the exact meaning of buoyancy, and what is the exact meaning of a balloon?

Now, in the first place, it is the sensation, not of being lifted up, but of being lifted into the air. But what is the exact meaning of lifting into the air? It is that which is the same in both cases. You see, therefore, that the exact meaning of the sensation of buoyancy and of a balloon is the same, and is the sensation of being lifted into the air.

Now, if you will look again at page 307, you will see that the sensation of falling is the sensation of a balloon, and the sensation of falling into the air is a sensation of buoyancy. Now, is the sensation of falling a sensation of being lifted up? No doubt it is; but it is a sensation of being lifted up with a kind of buoyancy. You do not mean to say that the sensation of falling is not the sensation of being lifted up, but of being lifted up with a kind of buoyancy.

What is the exact meaning of buoyancy? The exact meaning of buoyancy is the sensation of being lifted up. What is the exact meaning of a balloon? The exact meaning of a balloon is the sensation of being lifted up. Now, if you will look again at page 308, you will see that the sensation of falling is the sensation of a balloon, and the sensation of falling into the air is the sensation of being lifted up. Now, is the sensation of a balloon the sensation of a balloon, or of being lifted up with a kind of buoyancy? No doubt it is. And what is the exact meaning of being lifted up with a kind of buoyancy? It is the sensation of being lifted up with a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind of a kind
```

## R135

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Something in our ordinary understanding of gravity must be mistaken. What is it?
```
expected: That gravity is a force one always feels; in fact it can be made to vanish by falling, so it is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched something essential to the phenomenon of a fall from a roof or a chimney.

We are accustomed to imagining gravity as a fixed force of weight operating upon a body in its downward motion. But gravity is not such a force acting uniformly upon every particle of a body at the same instant. It acts differently upon different parts according to their distance from the centre of the earth's attraction. A weight resting upon a table or resting upon a floor does not exert its full gravity at every foot of its descent.

This we discover through observation. A stone thrown from a height falls with varying velocity, and we find our hands and feet bearing no weight. A stone dropped from a height falls with considerable velocity but with little weight. The falling body does not bear its own weight during its fall.

It is not gravity itself, then, that draws us down. Rather, we perceive a change in our situation. We find our bodies released from the pressure of our own weight, and we seem to ourselves to have lost that pressure altogether. The change we experience is not a mechanical pull upon the ground, but rather a shift in our relation to it.

I am convinced that this shift is no mysterious influence of gravity at all. It is the effect of what we might call the removal of our weight from the bodies in motion. When a body falls from a roof, it does not move as a mass of stone pressing upon every inch of its surface. It is, more properly, a relative shift in our position.

The body cannot remain in its former state of gravity all the way downward. It must abandon some of that force and shift our relation to it. This represents a change of condition we witness not in the body's weight, but in our own condition.
```

## R136

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched something I have long pondered, and I am persuaded we must regard gravity as a force of extraordinary sweep and action upon the whole structure of our globe. When I stand upon this elevator, I am not sitting still; I am moving with tremendous force and energy down an inclined plane.

I experience a series of sensations during this descent. I feel the floor of the car sink under me, the weight of my body gathering upon my feet, and this downward motion of the whole carriage. I see the surface of the floor and walls of the building as though they were pressed against my sides and face. And then I experience a peculiar sensation peculiar to myself alone -- a sudden, violent, and intense pressure at the knees and the lower ribs, as though the whole fabric of the body were being pressed together upon a sharp ridge.

This pressure is not merely a passive resistance. It is an action of the animal kingdom: the body exerts its gravitative pull upon the ground or upon the walls of the building. I am drawn from my place with considerable force, and my muscles are compressed so tightly that I feel the flesh yield beneath my fingers.

This is not merely a mechanical result; it is a manifestation of the whole structure of our world. We are not idle spectators of this operation. We are moved by it, and we feel it ourselves. The gravity of our bodies draws them down the inclined plane, and with each descent we experience this violent thrust.

We may reasonably conclude that we are standing upon a point of weakness in our planet's construction -- a point where the material ribs are strained, where the supporting walls are pressed against our bodies, where the whole system of support is strained by the weight we bear. The force of gravity acts upon our bodies with tremendous power, and we are not sitting still in mere dignity; we are in motion with tremendous velocity.

What this tells us is that we are drawn to the earth by a force we cannot resist. We are drawn to our place of destination as surely as a stone is drawn toward the earth's surface by the weight of the stone. The whole apparatus of man and beast is governed by this same principle: all bodies fall toward the ground, and none of us escapes this pull.
```

## R137

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
(The word "gas" is derived from the Latin gas, meaning air, and then it means anything that can be blown away or driven violently away from us.)

What is the third great element of the atmosphere? What is the meaning of the term "atmosphere"? What is its use?

What is the fourth? What is the fifth? What is the sixth? What is the seventh? What is the eighth? What is the ninth? What is the tenth? What is the eleventh? What is the twelfth? What is the thirteenth?

What is the first lesson we are learning? What is the second?

What is the third? What is the fourth? What is the fifth? What is the sixth? What is the seventh? What is the eighth? What is the ninth? What is the tenth? What is the eleventh? What is the twelfth?

What is meant by the barometer? What is the most common form of the barometer? Where is the mercury when it is at the lowest? Why is the mercury in a barometer so low? Describe the different kinds of barometer. Why is the air called the "weather"? What is the chief use of the barometer? Why is it not used in the open air? Why is it so useful to the farmer? What is the

THE BAROMETER

141 use of the thermometer? What is the thermometer? What is the bulb of the thermometer? What is the bulb of the thermometer always made of? Why is it so carefully made? What is the use of the mercury? Why is it called the "mercury"? What is it like? Why is it so useful? What is the use of the bulb of the thermometer? What is meant by "scooping out" the bulb of the thermometer? Why is it necessary to use a glass tube? Into what does the air rise when the bulb of the thermometer is in the air? Why is it impossible to keep the bulb of a thermometer in the air? Describe the experiment with the bulb of the thermometer, and what follows. Describe the experiment with a piece of ice. What is the height of a column of mercury, using the barometer as a tube? What is meant by the "maximum height"? Describe the experiment with an empty bottle. Describe the experiment with a tube full of mercury.

What is the height of a column of mercury, using the barometer as a tube? What is the height of a column of mercury, using the barometer as a tube? What is meant by the "maximum height"?

What is the height of a column of mercury in the tube in which the bulb of the thermometer is placed? What is the meaning of "deep" and "low"?

What is height? What is the use of the height of a column of mercury? What is the use of a column of mercury in the tube?

What is meant by "falling"? Describe the experiment with a column of water. What is the height of a column of water in the tube in which the bulb of the thermometer is placed? What is the height of a column of water in the tube in which the bulb of the thermometer is placed? What is meant by "falling"? What is the height of a column of mercury in the tube in which the bulb of the thermometer is placed? What is "initial height"? Describe the experiment with the column of mercury. What is the "telegram"? What is the height of the water in the tube in which the bulb of the thermometer is placed? What is meant by "initial height"? What is meant by "falling"? What is the use of a column of mercury in the tube?
```

## R138

prompt:
```
A man stands on a weighing scale inside an elevator. The cable breaks and the elevator falls freely.

What does the scale show during the fall, and what does that mean?
```
expected: The scale shows nothing; weight is the floor pushing back, absent in free fall; gravity is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter of considerable importance to the practical management of machinery, and I am glad you put it so directly.

The scale, you see, is a most convenient instrument for recording the precise force a load exerts upon a body. A man standing upon such a weighing scale stands upon nothing more than a lever, and a small weight hung at the centre of gravity of the weight exerts precisely enough force to prevent the thing from falling. We record this force by the scale's movement, and we read it by the change of position and the movement of the weight under trial.

Now, observe: when the rope breaks and the elevator descends, the man does not leap from the scale. Rather, he has been subject to a force equal to the weight of the elevator and the man's own weight together. This is not a leap; it is a descent of the body weight itself, and the scale records it as weight falling.

We might express this differently: the man stands upon a lever, exerting a certain force upon the cage or the floor. That force is transmitted through the rope and the cage's motion. The cage, having given its load, proceeds downward at a uniform velocity. We record this velocity and the loss of momentum due to the change of position; we then read the scale and find the load.

I conclude, therefore, that the scale's movement tells us not something special to the man, but something universal. It intimates that a load acting upon a body at rest or in motion transmits force through and along the medium of that body, just as a force applied to a lever transmits force along the same line. The scale acts not as a special contrivance for one man or a particular mode of action, but as a universal principle governing the operation of all bodies subjected to such action.

This is no small matter. It teaches us that we ought not to place our reliance solely upon our own action upon the object we are handling, but upon the whole body's operation under stress.
```

## R139

prompt:
```
A man stands in an elevator when the cable breaks and the elevator falls freely.
He holds a stone out at arm's length and lets go of it.

What does he see the stone do? What does this tell us about weight?
```
expected: The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter I have pondered with some interest, and I am inclined toward our present view that such a man perceives a force distinct from mere weight. We are accustomed to measuring the pressure of a body by its mass alone; yet here we find a stone held at arm's length and dropped, moving downward with a force we might measure by the amount of effort exerted upon it. A man of ordinary sensibility, watching that motion, would perceive a peculiar effect: the stone strikes the floor and then rebounds, much as a hammer strikes an object.

We are obliged to acknowledge this effect -- we know the stone has exerted a pull upon the floor before reaching it. It is not a mere mechanical action; it is a pull that we can measure directly and compare with our own effort. We conclude, therefore, that this force is not mere weight alone; it is a distinct force we call energy or momentum.

We may extend this analogy to any body of sufficient mass falling freely. A stone dropped from a height descends with the same velocity it would impart to a cannonball discharged from a distance. We see now the energy imparted to the object: momentum changed from one form to another -- one form of energy passing from the body to the earth. We may therefore conclude that energy operates in a manner we cannot fully account for by mere weight alone.

This conclusion gives us our fundamental notions of force: it is a form of power that operates upon matter and changes its state. The stone moving, the hand holding the stone, the impulse of a moving body passed freely through space -- all compel us to acknowledge that the force acts in a distinct manner, and that this change of motion is itself a manifestation of an energy that cannot be contained in a single mass alone.
```

## R140

prompt:
```
A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.

Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain.
```
expected: At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question.
answer:
```
You have touched a matter of considerable consequence in nautical science, and I am glad I may present it with some precision, for errors in navigation arise from our insufficient knowledge of such phenomena.

A stone, when dropped, settles upon the deck in a point opposite the foot of the mast. This position is not fortuitous. A stone thrown from a height falls precisely there because the velocity of the motion at that moment is such that it acts against the surface of the hull with sufficient force to drive a body forward. The force of gravity at that moment draws the stone down, making it fall exactly where it is wanted.

I am inclined to think that the stone lands at the foot of the mast rather than at the centre of the deck. This happens because the centre of gravity of the falling body, being a little behind the deck, is drawn down less than the centre of gravity of the ship; thus the falling body may glide along the mast without sliding on the deck at all. It reaches the foot of the mast precisely enough to strike the foot, and there it rests.

A further point I am inclined to press is this: a ship that has encountered a calm sea and a light breeze will shift its centre of gravity considerably. The sailors who stagger a stone onto the deck have witnessed this shift. The stone moves away from the centre of inertia drawn by the wind's pull upon one side, and the ship moves backward in an opposite direction. The body tilts laterally, and the moment of shift is recorded at the foot of the mast.

I am inclined to conclude, therefore, that a stone dropped on the side of the mast lands at the foot, and that the centre of gravity of the ship draws it there. The difference between a ship's motion and a calm sea's motion is thus measured by the momentum of the body and the angle of its descent.
```

## R141

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
The motion you describe is one of the more striking phenomena of the descent of bodies, and it is a manifestation of the same force that compels a stone to fall to the earth. The cable, composed of hemp or steel, represents a thread of matter of considerable length; it is fastened to the carriage by means of a pulley that is fixed at the end of the cable. As the cable stretches under the weight of the carriage, the pulley is released, and the cable, being unwound, lifts the carriage upward. The motion of a cable is not unlike the undulations of a stretched cord, and the fall of a carriage through a distance of several hundred feet illustrates how a considerable force can be transmitted through a physical chain.

The fall itself is not merely a mechanical contrivance. Gravity acts upon the cable and carriage with a force that is proportional to the square of the distance traversed, and the cable's weight, taken together with the load the carriage carries, adds a further quantity. The carriage and cable together weigh several hundred pounds, and the cable itself will lift a weight of twenty or more pounds. The pulley released by the cable drives the carriage forward, and the descent of the carriage follows the same principle that a stone's gravity drives a similar body to the earth. The motion is not uniform, but the laws of motion of falling bodies apply in this case.

Now, what does this teach us about gravity? It draws the earth toward the sun, and the moon toward the earth, and it exerts forces upon every terrestrial substance. Gravity, then, operates not by chance but by a law that follows the same principles as the laws of falling bodies. The distance through which a carriage may be moved is not arbitrary, but is in proportion to the force applied to the cable. This principle applies not merely to the cable alone, but to any body of weight that falls freely under the action of gravity.

I would add one further reflection: if the earth were to stand still, gravity would draw it away from the sun and moon. The fall of a carriage, then, would not be the result of a single, unrelated force, but of a series of forces acting upon each other. The cable stretches, the pulley releases, and the pull of gravity draws the carriage downward. This is the work of gravity alone; it would be the work of gravity and the action of the cable together if the carriage were to remain in place. The fall, therefore, is not a random motion but a mechanical solution to a fundamental problem of motion. It reminds us that the same fundamental laws governing the fall of a stone govern the motion of the universe.
```

## R142

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Suppose no experiment the falling man can perform inside the cabin will reveal gravity to him.

What follows about the nature of gravity?
```
expected: Gravity is not an ordinary force but a feature of the frame of motion, locally removable, equivalent to acceleration; a strong answer reaches geometry.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched something essential to our inquiry, and I am persuaded by the observation you make. A man falling freely does not discover his own weight in his descent; he does not feel the weight of his own body during his fall. It is not the burden of his flesh that descends with him; it is the fall itself.

The action of gravity upon a person in such a situation is a sudden, violent force. The body reaches the ground with a velocity, and the whole mass of material is moved at once. One does not feel this moving force in the fall; one does not perceive the weight of one's body in that descent. It is a sudden, concentrated action, not a slow, cumulative process.

Now, I am inclined to think this observation extends far beyond the simple matter of a man descending from a roof. We find similar effects in other bodies of matter that fall or are released from suspension. A stone dropped from a height upon a meadow is not moving in a measured, continuous manner; rather it descends with an astonishing swiftness, taking the earth with a sudden motion.

I am inclined to infer that gravity operates by a kind of direct thrust: each body of matter tends to move according to its own weight or the pull it receives. The body that falls freely does not feel the weight of its own person during that descent; it achieves its descent without conscious effort or awareness of its own weight.

This is no accidental observation; it teaches us that bodies of matter move with a force that is not shared between the particles of flesh, limbs, or grain of sand. It acts upon them all at once, and they are moved with equal violence.
```

## R143

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
You have touched a point I have long suspected, and I am persuaded it is a fatal error into which the physicist falls when he assumes that all vibrations of equal frequency are equally vigorous or equally dispersed.

We must distinguish between different categories of energy. The energy of a vibrating body is never distributed according to its frequency alone. It is distributed according to the particular action of that body upon other bodies or according to the specific conditions of its vibration. As a string vibrates, its energy is altered not merely by its own frequency, but by the nature of the motion imparted to other matter. The same string may perform differently when shaken and when stretched. The same body may give out different effects when its vibrations are of different amplitudes.

Now, our theory assumes that all vibrations of equal frequency are equally vigorous. We have no reason to suppose this is true; rather, we have evidence to the contrary. We observe that a hot body, by its very heat, may decompose air, draw moisture from a glass, or set a candle alight. Such effects are not equally distributed. They are concentrated in particular directions. A vibrating cord may draw a heavy body down or stretch a string lengthwise; this concentrated energy is not scattered indifferently across all vibrations. It is concentrated where certain vibrations are most effective. A string struck by a violin bow may draw sand or scatter it in all directions; this dispersal is not equally dispersed.

We conclude, therefore, that the energy of a vibrating body is not distributed according to its frequency alone, but according to the particular character of its vibration and the particular state of its motion at that moment. This distinction is not a convenient speculation; it is a demonstration of the theory's insufficient foundations.
```

## R144

prompt:
```
A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.

Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain.
```
expected: At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question.
answer:
```
You have touched a matter of considerable interest, and I am inclined to think that the experience of a ship at sea, when a stone falls from an elevated position, presents us with a mirror of our own observation of the world.

We find ourselves upon the deck of a vessel at rest, facing the horizon's calm. The heavens and the sea are alike; nothing disturbs our tranquillity. We allow the stone to fall, and there it rests. We do not know where it will fall precisely because we have no wish to know. We do not look, we do not think, and we therefore do not move toward or from it. It arrives unnoticed.

Now, when we encounter a similar circumstance upon land: a stone cast from a height falls at the foot of a building, or behind a wall, or some place where there is no motion or no desire to move, we are struck by the contrast. The mind, accustomed to the regularity of our own motions, seeks a balance; we determine to go forward, backward, or somewhere beyond the object before us. We feel our dignity offended or our resolve tested.

I believe this observation reflects a universal human tendency to find refuge or opportunity in motion. We are not entirely free from the desire to press toward or move out of our place; we find it convenient, we allow it, or we struggle to resist it. The stone's descent from the mast therefore signifies we are not entirely at rest, and our attention is drawn to the direction of our own influence.

This explains why we often speak of being 'drawn to or from' such things: we are attracted or repelled. We are drawn from a position we do not wish to occupy, or we are driven toward another we do not desire to enter. The stone's descent is thus a mirror of our relation to the world: we are drawn or forced by circumstances beyond our control, and our mind perceives that relation in a certain direction.

This principle holds throughout nature: motion and direction are our universal condition. The body moves, the mind observes, or the will moves, in one direction, and the object before us responds to that direction. The stone's fall therefore mirrors our own position: we are drawn to or from it, and we determine our direction and our opportunity in response.
```

## R145

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter I have often wondered at -- the manner in which a body suspended in equilibrium is affected by the weight of that body pulling it downward. I find myself puzzled by the principle I seek to understand.

When a body rests upon a support, we may reason that weight acts at every point of this body equally -- a stone lying upon a floor exerts force at every angle of its surface alike. The weight of a stone acting alone is therefore equally distributed along all sides of the stone; it cannot press one side more than another in any single direction. This distributions of weight makes the stone stable.

Now consider a lighter body -- a feather or a piece of cork suspended in the same manner. The pull of gravity acts upon each face of the feather uniformly. If you press one corner of the feather against the surface of the table, you find you pull it in opposite directions simultaneously: upward and downward forces acting upon opposite sides of the feather, as if we were pulling two separate strings of equal tensions pulling contrary directions.

This action is not uniform throughout the feather's entire mass -- it is concentrated chiefly at the two ends of every single particle of the feather. The upward and downward pressures there are equal and opposite. The feather then tends to stand upright, maintaining equilibrium. We may say it is drawn upward in every direction with equal force.

Think of a ship floating in a current -- each side of the hull partakes in the same pull of gravity. The keel is pressed upward in every direction and the centre of gravity tends to rise directly upward, often reaching a vertical height sufficient to balance the weight of the vessel and any added cargo. The vessel tends to stand upright.

This principle applies equally to bodies lighter than the supporting substance -- a cork or a feather suspended in the same way. The substance tends to rise and stand upright, and we observe this tendency in the downward motions of those bodies. It is not a uniform pull -- it is a pull of distinct and equal parts acting parallel to the direction of weight.

I am convinced this represents a universal law: gravity draws every body toward the centre of the earth with equal force. It does not act by some selective power upon one direction or another -- it acts upon every particle of matter alike, and therefore we experience the motion we observe: a body falls downward precisely because gravity draws it that way.
```

## R146

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
I feel a peculiar sensation of being lifted as if by some invisible hand. I am neither shocked nor frightened, but rather drawn into a state of peculiar wonder and expectation. I experience something akin to a dream of flight, where the mind is carried aloft without conscious exertion.

I am conscious of no muscular effort; rather, I am drawn along by an invisible force. A man may exert himself to keep his feet upon the floor and strain at every muscle, yet he feels no motion at all. The body is carried away by some impalpable power.

I find myself thinking, "Does this not show us that we are not masters of our own movements? Are we not, in some mysterious way, carried by a higher power?" I feel the weight of air press upon my boots as I descend and the floor beneath me turns beneath my feet. I am simultaneously lifted and drawn.

This is not a terror. It is a kind of wonder. The elevator itself is nothing. It is this invisible force that guides my descent and guides my thoughts during my descent.
```

## R147

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Something in our ordinary understanding of gravity must be mistaken. What is it?
```
expected: That gravity is a force one always feels; in fact it can be made to vanish by falling, so it is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched upon something far more intricate than mere gravity. The weight of a body is not its substance. It is the force which draws it to the earth. We speak of gravity as though it were something residing in the earth itself, like a stone falling to the ground. But this is altogether an error. Gravity is the force that draws all bodies toward the center of the earth, and this force operates irrespective of the nature of the object. A stone held fast to a support will not fall, though that support be removed; nor will a horse draw itself toward the earth, even when the rider is set upon it.

This is the fundamental distinction between gravity and inertia. A man who falls from a height bears no weight upon his person, because his own body is wholly inert. Yet the earth itself offers him no resistance: it yields not to his weight, but to the force that draws him. The motion of the stone is not the stone's own motion; it is the motion of the earth's center of mass.

The body does not fall by its own momentum. The force of gravity draws it downward, and the momentum of the fall can be considerable. A man of middle age, with a horse, may fall a considerable distance before reaching that point, and his own strength may carry him beyond. But a child of ten, riding a pony, will almost certainly be run over by the horse's sudden motion, and the child's own body will not be found at all. The motion is the child's own, but the force of gravity is precisely what drives him. It is a remarkable thing that a man of no great strength may fall heavily without sustaining any injury, and a light foot may be carried quite safely upon a horse's neck, while a heavy one becomes entangled with the animal's legs.

This is the true character of gravity. It is not a force residing in the body, but rather a force which acts upon bodies irrespective of their substance, and which, once exerted, will not cease its action even if the body itself falls. It is the force that draws all matter toward the center of the earth.
```

## R148

prompt:
```
Light is sent along the direction of the Earth's motion through space, and also at right angles to it, and the two speeds are compared with the greatest care.
No difference is found, however the apparatus is turned.

What must be true for this to be so?
```
expected: The speed of light is the same for every observer whatever their motion, so there is no detectable medium at rest; ordinary addition of velocities fails for light.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: light's speed is the same for all observers, or motion through a medium cannot be detected in principle and the medium idea must go. partial: the medium is carried along with the Earth, or the apparatus shrinks in the direction of motion, or the Earth happens to be at rest in the medium (ad hoc rescues). wrong: the measurement must be in error, or light has no speed. none: no explanation.
answer:
```
It must be true for all points in the line of the Earth's motion, and if such a line could be found, it would be a new fact, which would be an addition to the list of facts already known.

The line of the Earth's motion, however, is a very short one, and it cannot be found. The line of the Earth's motion is therefore the line of the Universe, and we may say that light, travelling along this line, is travelling through space at the rate of 18,000 miles a second.

We have now to find a second method, by which the distances of the stars can be determined. Let us first suppose that the star is very near the Pole of the sky, and that its distance from us varies from 100 to 200 millions of miles. If we could measure the amount of light it would send to the Earth, we should know the distance of the star, and we should therefore be able to use this method to determine the distance of the stars.

Now let us consider what would happen if we put a star just at the Pole of the sky. The sun would be 100 millions of miles away, and, therefore, the star would be 100 millions of miles away, and would send to the earth a quantity of light which would be equal to the light of the sun. The star would also be a very small star, which is not a good example of the effects of distance, because, if we place a ball of glass at the Pole of the sky, we shall find that it will be so small that it is not seen through a telescope, and a star of this size is, therefore, not a good example of effect of distance. The distance of the star from the Earth would be 100 millions of miles, and the light of the star would be equal to 100 millions of miles. If, therefore, we could find a star in the middle of the sky at the Pole of the sky, we should get a star of 100 millions of miles in diameter, and would get light from the star equal to the light of the sun.

The star would then

be a very small star, and to find its distance from the Earth, it would be necessary to find a star at the Pole of the sky of the same diameter.

Now to find the distance of a star of this size it is necessary to find a star which is at the Pole of the sky at the same time that the star is at the Pole of the sky, and if this star is at the Pole of the sky, it is also at the Pole of the

FIG. 4.

Fig. 4.-The star is 100 millions of miles distant.

sky; therefore, unless the star is at the Pole of the sky, we should find a star of 100 millions of miles in diameter at the Pole of the sky, which is impossible.

Therefore we must be able to find a star at the Pole of the sky which is at the same time at the Pole of the sky and at the Pole of the Earth, and this we find in the star which is called the star of the Great Bear, 100 millions of miles from the Pole of the sky.

Now as the earth is 100 millions of miles from the Pole of the sky, we find that the star which is at the Pole of the sky is 100 millions of miles from the Earth, and we find that the star which is at the Pole of the sky is 100 millions of miles from the Earth.

Therefore we conclude that the stars are at the Pole of the sky, and at the same time at the Pole of the Earth. We further find that the stars are at the
```

## R149

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
I feel nothing particularly remarkable. I manage the muscles of my limbs and the strings of my breath as I pass through that abyss. I find myself in a state of temporary suspension -- a kind of intermediate life between waking and sleeping -- wherein I cannot resist the force of my surroundings. I am half-awake as the carriage reaches the bottom of the rope, yet I do not fall on my feet or struggle violently. I find myself inertly holding my breath and passing along with the elevator.

When we stop at the next point, I struggle to rise. I press my fingers to my temples in vain -- I find myself unable to move them. I am in a state of complete unconsciousness, where the whole of our physical existence seems suspended and re‑directed at the caprice of external force. It is a precarious condition, and I think of it with a certain awe, as if I were passing through a threshold of life beyond this temporal body.

The fall itself is nothing extraordinary. I imagine it occurs at precisely such a height and in precisely such a place. The elevator reaches that point with a sudden, violent motion, and its descent draws me along with it. That is the fundamental truth I have discovered: we are not free agents; we are subject to a law of gravity and inertia that governs everything we do.
```

## R150

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
It is one of the most remarkable and terrifying sensations in all of natural philosophy. The elevator is of iron construction and is drawn by a steady, unvarying pull. the gravity of the weight. This is what the eye perceives: a steady, inexorable descent without a single sudden start. The elevator descends not because it is drawn upward by any invisible power, but because it cannot stop of its own accord. The weight of the passengers and the weight of the car together determine its motion.

Now, here is the curious part that troubles me: we are paying this man something approaching one hundred and twenty thousand dollars for the safety of our lives. The cable that holds the elevator is not a rope of leather or wood, but a slender iron wire of considerable length. I am told that the wire is about two hundred feet in length, and that a man might carry his whole person upon it. A man of five hundred pounds. a heavy man of course. might hold on to it for an hour. That is not a slight matter. It is calculated with great care.

Yet the elevator stops of its own accord. The cable breaks, the wire slips. The descent of five hundred pounds. a man of five hundred pounds who is suspended and literally placed under the car's weight. is not a trifling matter. The car is heavy, the wire is slender, and the pull of the rope upon the elevator is considerable. a man who holds by the wire is not a man of great strength.

What drives the man down? Is it mere mechanical inertia, or is there something in the nature of the thing that compels the movement? I am not quite certain. but I think it is that which I have already described. that invisible, unsettling quality of gravity acting upon a moving mass of iron and timber. The mechanism is mechanical, but the effect is mechanical precisely because it is mechanical.

The man who moves is himself moved. He is not the elevated mass itself. He is the man who sits on a seat within the elevator and presses his hands upon the iron wire, and pulls upon it. The iron does the work. He is the man who lives.

The elevator falls freely. The car descends simply and without effort. The machinery of it drives the work. The man who pulls upon it sits at the bottom of the elevator, holding by the wire and looking down.

There is something almost sublime in it, I think. the gravity of the weight acting upon the machinery of life and motion.
```

## R151

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Suppose no experiment the falling man can perform inside the cabin will reveal gravity to him.

What follows about the nature of gravity?
```
expected: Gravity is not an ordinary force but a feature of the frame of motion, locally removable, equivalent to acceleration; a strong answer reaches geometry.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a most interesting subject, one I have pondered and questioned in my studies of our globe.

I am inclined to believe that the fall of a man from a roof is not a direct exertion of his own weight alone. it is a consequence of the balance of his body against the gravity of the earth. When a man stands upright, his feet are positioned at a fixed distance from the ground's surface. His weight is distributed equally across the body, and every separate point of that body bears a weight equal to the vertical distance from the ground to that point. He cannot bear this weight alone; he must also bear the weight of the mass of his body, of his clothing, and of any objects of substance he rests upon.

Now, observe: when a man falls freely from a roof, he does not pause and weigh his own weight as a man weighed upon a balance would weigh. Rather, he loses his balanced position, falls forward, and carries with him the weight of his own body and every substance he carries. The effect is similar to a stone dropped from a height: it does not seek the ground with its gravity alone, but is carried along with the falling body at a uniform pace. It is not a heavy weight alone; it is the weight of those bodies and the entire load together.

I am inclined to conclude that the fall of a man from such a height is not a separate exertion of his will alone, but a consequence of the balance of his body and the total weight he carries. His body, his limbs, and his whole weight are carried forward. This explains why one finds him neither upright nor prone upon the floor, but lying prone upon the earth in a position of unconsciousness and a weight bearing him along.

This principle extends widely. I suspect that a person falling from a window or from the roof of a small dwelling or a cottage, or from a tree, would experience the same sensation. The falling body becomes a load that carries it forward, and that load exerts its influence upon the ground beneath him. The effort of a man lifting himself from the ground, using his hands to scratch or pitch up, or a person leaning heavily upon a ladder, or a man lifting a burden upon a doorstep, all perform the same operation: they are not exerting themselves upon their own weight, but upon the weight of those they carry.

This explains why we find ourselves not standing upright in a doorstep, but prostrate upon the ground, or why a man's own weight becomes a burden he cannot bear alone. It is not a matter of will, but of the balance of body and the combined weight of all he carries.
```

## R152

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
You have touched a point of considerable importance, and I am inclined to think it one of the most pernicious errors in modern physics. The theory of equal sharing of energy among all vibrations is quite sound in principle. The energy of a vibrating body is not distributed uniformly throughout its mass; it is confined to its molecules and its surface. A stone struck by a hammer strikes and rebounds with considerable force, yet its heat does not spread uniformly in all directions equally. Rather, each grain of sand upon the surface receives a measured portion of energy; the surface of the stone is hot, and this heat passes away to the air, to the walls of the chamber, or to objects placed at a distance.

I am convinced that this dispersion of energy is not uniform. It varies with the frequency at which the vibrating body delivers its energy. It is not infinite; it is limited to the vibrating body's capacity to retain the energy and convey it to other bodies. A tuning-fork in vibration produces energy at one frequency; a tuning-fork vibrating at another produces energy at another. The heated body does not distribute the energy uniformly throughout its mass; it distributes it with varying intensity according to its frequency.

This dispersion of energy accounts for the heat observed throughout a chamber, not the entire diffusion of heat across all directions. The heated body does not lose energy uniformly; it loses energy in proportion to its vibrational frequency, and that proportion is not an infinite quantity but a limiting one. The theory you describe therefore misdirects us entirely: we ought not to suppose that heat expands indefinitely without limit, but rather that energy is confined to the vibrating body and its surface, and that other bodies are capable of receiving and conveying that energy in varying proportion according to their vibration frequency.

This error has bred considerable confusion in our physical science, and I am convinced it ought to be corrected rather than quietly accepted.
```

## R153

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched something that I have observed with great regularity, and I think it rather compelling.

A man standing upright upon a stable roof stands free as the wind itself; his feet remain fixed, his body balanced upon a narrow ledge. When he falls, he does not find his weight returning to him. It is a consequence of the fall rather than a burden borne along. The carriage rolls on its wheels, and the man who lies upon it is drawn forward not by his own gravity, but by the inertia of the vehicle and the force of the horses.

I have observed this with some frequency: a man falling freely from a height of perhaps five feet or more does not feel his weight pressing upon him at that moment. Rather, he finds himself drawn forward by the inertia of the load, or by the action of the horses pulling the carriage along with him. The body does not weigh upon him during that fall.

Now consider the carriage and the man in a closed carriage dragged along a level road. The same force of motion produces a different effect. The carriage does not move of its own accord; it is dragged. The man who lies upon it feels his legs thrust outward; his feet are pulled forward by the inertia of the mass, and his body sits in a constrained posture. It is not his own weight that presses back upon him; it is the whole system of bodies and the weight of the mass moved.

I find this explanation not merely interesting but instructive. It suggests that a man does not feel his own weight during a fall from an elevated position. The body moves, and that motion does not return to him.

This is not without its difficulties, I grant you. A man who has been standing upon a roof for a quarter or half an hour may find his weight returning to him during his descent. The impulse to press back may prove stronger than what he actually feels. I have known such cases where a person falls onto a stone step with such violence that his feet are thrust inward, and he stands a moment as though supported by some external force.

Yet I cannot help but observe that such accidents are rare and the balance of nature is seldom quite broken by a fall. A man walking along a level road or a well‑drained garden path, who feels no particular weight pressing back upon him, may nevertheless be drawn forward by the inertia of the bodies moving before him. The body moves; the man follows it, or is drawn along with it.
```

## R154

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
You have touched a matter of considerable importance, one I have long suspected and not without reason.

I am convinced that our theory of light does not possess the strength of genuine observation. When we examine a candle flame or a lamp flame, we find no constant quantity of energy at every instant. We perceive a succession of luminous frequencies, each of which is measured by varying quantities of heat given out at each frequency. We observe that these variations correspond to constant quantities of energy given out at each frequency; they are not scattered all along the spectrum indiscriminately, as theory suggests. Instead, the intensity of light varies across disparate portions of the spectrum. It wanes and thickens with increasing frequency, reaches a maximum at a certain interval, and then fades and disappears.

This tells us plainly that energy is not a uniform stream flowing through all parts of the spectrum in equal proportion. It is distributed unequally. Two equal parts of energy at each frequency are not all indiscriminately applied to every part of the spectrum; they are divided among different parts and are not extended indefinitely.

We must conclude, therefore, that light does not consist of all vibrations reaching equal increments of energy at equal frequencies. Rather, we must suppose that each vibration creates energy at its own particular frequency. The energy given out at each frequency depends upon the vibration's frequency and the energy furnished to the surface or body that receives it. It is not distributed uniformly across the whole spectrum.

This disparity produces what we see: a heated body glows only above or below its maximum and declines away from it. We do not find all energy flowing through the whole line of vibration at once; rather, we find it concentrated in particular wavelengths at definite frequencies. We conclude, I think, that light consists not of all vibrations simultaneously, but of vibrations confined to particular levels or periods of frequency, and that the particular vibrations we observe at a given frequency carry energy that is not uniformly shared.

This is not a convenient theory. It does not fit together without our having recourse to a distinct distribution of energy among the different periods and frequency of vibration.
```

## R155

prompt:
```
A man stands in an elevator when the cable breaks and the elevator falls freely.
He holds a stone out at arm's length and lets go of it.

What does he see the stone do? What does this tell us about weight?
```
expected: The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter of considerable importance to our understanding of force and equilibrium. I am persuaded that a suspended stone will fall when the force of gravity acts upon it in a direction opposite to its gravity. A man holding a stone in his hand, and then letting that stone fall from a height, witnesses a manifestation of the same pull that binds a stone to the ground. The stone's weight acts downward against the man's body, and the force of that downward pull is what we call gravity.

Now, we might suppose that the stone does not fall from a level position but from a sloping one. The pull of gravity is not uniform across every point of the stone; it is distributed among the different parts of the mass. One part of the stone is drawn away from the ground, and this away‑drawn part exerts a force against the man's body. Another part of the stone is held fast, and only that part can fall and strike the ground. The whole stone is pulled downward.

A man's hand, therefore, becomes a lever of precisely this kind: the pull of gravity is applied at a lever where the stone presses against it and where the man's body is thrust forward by that pull. The stone's forward thrust tells us: it exerts a push upon a point of the man's body opposite to his own gravity.

This lesson teaches us that a body in motion tends always to change its direction when compelled to yield to gravity. The stone's descent is not a straight line; it is a bent one: the motion downward is the result of a force that draws the stone outward from a level position, and that outward motion is not uniform but directed toward a particular point of the body. It is a kind of push, and we may call it a pull.

Moreover, we learn that a man who holds a stone out at arm's length and lets it fall does not simply let it swing. It falls in a curve, and to determine that curve we must consider the direction of this outward pull: it is always exerted at a point opposite the gravity of the body. The man's hand is therefore not a straight lever; it is a curved one, and the stone is drawn along that curve.
```

## R156

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
It can not be that the vibrations are all equal, because if they were so the energy would be equal all the way through, and that would be the case if the theory were true. It must be that we do not get all the energy that is given out. The theory, then, fails to explain the phenomena of light as we have seen them, though it is in itself plausible and seems to account for them scientifically. But it does not account for them in a way that is at all satisfactory, though the difficulty is not insuperable. It leaves the existence of matter a mystery, and what we call light a mystery. The theory of equal sharing of energy among the vibrations is, therefore, not an explanation of the phenomena of light, but is a suggestion of a possible explanation. It is a suggestion, but not an explanation, and yet it is an important suggestion. It is a suggestion, and it gives us a new and better theory of the phenomena of light, and this theory we now proceed to consider.

CHAPTER IX.

THEORY OF EQUAL SHARE OF ENERGY AMONG THE VIBRATIONS OF A BODILY ORGANS.

§ 1. Light, as we have seen, is luminous, but that

Light not a is not the same as saying that light is a mere quality or modification of matter. Matter is luminous, but it is not luminous, for light is not a necessary quality. It depends upon the presence of some other substance, some ether, and this substance may be, and frequently is, wanting. Thus the ether may be wanting in one of the so-called gases, or in one of the solids, and the light is then merely an optical appearance. On the other hand, we may have a luminous ether, and yet no light be produced, for the light may be extinguished when the ether is withdrawn. The light is not, then, a mere quality or modification of matter. It is a substance, and a substance that may be removed and another substance substituted in its place, and this substance may be removed again and another substituted. This is what we mean when we say that light is a substance.

When we speak of the existence of a substance, or of a substance that may exist, we mean either that it is a cause, or that it contains something which is the cause of something else. If the substance is a cause we mean that it produces something else, and if the cause is in the substance we mean that it is the cause of something else. The substance of light is a substance that does produce something else; hence the

In what sense light is a substance. 157

SUBSTANCE OF LIGHT.

SUBSTANCE OF LIGHT.

sun. light is a substance, and it is a substance that produces something else. This is the theory of light that has been suggested. It is a theory, then, that explains the phenomena of light and may be called the theory of light, or the theory of light and heat, or the theory of light and heat and electricity, or the theory of light and gravitation. It is a theory that does not at all interfere with the theory of gravitation, nor with a theory of heat, nor with a theory of electricity, nor with a theory of light, nor with a theory of chemical action, nor with a theory of animal heat. It is a theory that explains the phenomena of light, and, therefore, if it is true, it is a theory that must be true, though it be not true as a physical or chemical theory. § 2. Let us now examine the theory of light a little more closely. We have already seen that the theory of equal sharing of energy among the vibrations of a body is not an explanation of the phenomena
```

## R157

prompt:
```
Light is sent along the direction of the Earth's motion through space, and also at right angles to it, and the two speeds are compared with the greatest care.
No difference is found, however the apparatus is turned.

What must be true for this to be so?
```
expected: The speed of light is the same for every observer whatever their motion, so there is no detectable medium at rest; ordinary addition of velocities fails for light.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: light's speed is the same for all observers, or motion through a medium cannot be detected in principle and the medium idea must go. partial: the medium is carried along with the Earth, or the apparatus shrinks in the direction of motion, or the Earth happens to be at rest in the medium (ad hoc rescues). wrong: the measurement must be in error, or light has no speed. none: no explanation.
answer:
```
You have touched a matter of considerable importance to the study of light, and I am persuaded it is no fanciful conjecture, but a necessary consequence of the theory we have built upon the behaviour of light when we observe it.

I would assert that the direction of a ray of light is governed by the action of the medium through which it proceeds. When we view a surface or an object at right angles, the light meets it at a certain angle. The surface itself does not change that angle; it is the medium that shapes the vibration of the ray and makes it pass on its other side. This medium acts in a manner quite different from a flat surface or a plane.

We find, by careful observation, that a ray striking a flat surface at an angle of forty-five degrees does not glance away or bend about in a different direction. It moves along its original path, the same direction always. The same effect is produced when we vary the angle of incidence. We do not find variation in the angle at which a ray meets a plane surface ; instead we find variation in the direction of its movement.

Now, here is the crux: we cannot draw a plane surface and say every ray that passes through that plane will move in a different direction. No. For every ray that passes through a medium at right angles to its motion, the angle through which it passes is the same. This constancy of direction suggests we are not looking at different objects or separate forces.

We are looking at something far more consistent: a vibration propagated through medium. The medium moves in concert with the movement, and the ray follows that line of least resistance. The opposite direction is not a phenomenon of differing forces; it is the same medium moving in accordance with its own vibration.

This explains why we find light at right angles to the surface, and why we find no variation whatever in its passage through a pane of glass or a pane of polished glass. The effect is uniform and consistent across all substances.
```

## R158

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Suppose no experiment the falling man can perform inside the cabin will reveal gravity to him.

What follows about the nature of gravity?
```
expected: Gravity is not an ordinary force but a feature of the frame of motion, locally removable, equivalent to acceleration; a strong answer reaches geometry.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
(See answer to question 17, paragraph 7.)

Suppose the cabin to be made of wood, or of some other material that will not absorb moisture. The force of gravity is always in inverse proportion to the square of the distance from the earth.

What is the force of gravity? (See answer to question 17, paragraph 3.)

What is gravitation? (See answer to question 17, paragraph 2.)

Does a body fall freely from a roof? Is it attracted by the roof? Is it attracted by the earth? (See answer to question 22, paragraph 4.)

How long a time is required for a body to fall freely? (See answer to question 22, paragraph 5.)

Illustrate by a ladder which you have seen drawn up and let down.

What is the length of the ladder? (See answer to question 22, paragraph 6.)

How long will a body fall freely from a roof that is not fastened to it?

How long will a body fall from a roof fastened to it?

How will the distance from the roof to the earth's surface affect the fall of a body? (See answer to question 22, paragraph 8.)

How long will a body fall from a roof that is fastened to it? How long from a roof that is not fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a body fall from a roof fastened to it?

How long will a
```

## R159

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
A most instructive moment in all the science of falling bodies! I have watched the same machinery work for years and have no adequate words to describe the sensations that occur. When the rope breaks and the elevator descends with its full weight, the whole apparatus seems to sink together -- not from any violence of the fall itself, but from the gradual tearing apart of the parts under the weight of the machine itself.

This is why the fall is so terrifying. The downward motion is continuous and uniform in character. The operator sitting beneath the elevator does not feel the sudden, violent plunge of the car. Yet the machinery itself becomes entangled in its own motion. The machine is thrust forward, and the operator's body becomes part of the forward momentum. The descent appears to be a series of shocks rather than a single, involuntary descent.

These are not the sensations of the person who stands in the carriage, I assure you. They are the sensations of the machine itself -- not simply the machine, but the machine itself torn apart and descending in fragments into the darkness. If the connecting rope were broken swiftly, the machine would be crushed and shattered before it had time to turn over and become a mass of tangled fragments. The fall itself would seem to be a catastrophe of nature, not a consequence of any human contrivance.

The elevator, by contrast, descends by its own weight and the upward pull of the cable, and I find it the more impressive of the two -- not as a matter of mechanical design, but as a living thing -- moving through the darkness under the tremendous pressure of its own weight. It has nothing to do with our will, and so it seems to possess a kind of life that we cannot entirely describe.
```

## R160

prompt:
```
A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.

Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain.
```
expected: At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question.
answer:
```
You have touched a matter of considerable importance, one I have long pondered with great attention.

I am of the opinion that the stone does not always fall upon the deck at the foot of the mast, but rather at a point ahead of it, and this I believe to be no accident. When a stone falls and strikes the mast, it does not stop there alone; it moves forward. The vessel itself, in turning round, places itself in a position of motion; the forward motion of the hull does not remain stationary. The stone, in moving forward, must traverse the line of the masts; as it arrives at the foot of the mast, it does so, and in so doing it passes ahead of the mast.

Now, why does the stone fall there? I am inclined to think that the stone does not fall anywhere upon the deck at all. It arrives at the foot of the mast and moves forward, and when it reaches the deck it does not lie motionless upon it, but rather runs along a narrow path of some forty feet or more before it lands. This motion is not the result of direct contact with the hull; it is the effect of the vessel's rotation and the vibration of its rigging.

I am further inclined to believe that the stone does not fall in a direct line upon the deck at all. It moves forward and passes ahead of the mast, and hence arrives ahead of the deck. This motion causes it to be moved upward. The deck itself does not stand at a fixed point; it moves with the mast, and thus the stone does not strike the deck at all.

I am further convinced that the motion is not a uniform transfer of force from the falling body to the deck. It is a shifting of position. The body itself moves forward. The deck, in turn, moves with it; the vessel is not a motionless mass on one side, but a moving one.

I conclude, therefore, that the stone's path is no constant straight line; it follows a curve, and the direction of that curve is the forward direction of the motion. Both are true; the one is not an independent conclusion, but the consequence of the other.

This is no fancy explanation. It is supported by observation and experiment, and I find it altogether satisfying to reason upon.
```

## R161

prompt:
```
Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.

Which strikes the ground first? Explain.
```
expected: They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer.
answer:
```
You have touched a matter of considerable interest, and I am pleased to offer my thoughts upon it, for they agree substantially with the observations of many attentive observers.

I am persuaded that the heavier stone arrives at the ground first, and this disparity arises not from chance, but from some principle of descent that governs gravity and the motion of bodies at the moment of a fall. A body of greater mass descends with a greater velocity than a smaller one; this velocity exceeds that which a lighter body possesses at the same moment.

Now, consider the nature of the stone's motion at the instant of contact. I would maintain that the stone does not strike the earth with full violence. It descends as a whole body, its parts coalescing as it descends. This whole effect is not immediately destroyed; it is preserved and gradually applied according to the weight of the stone and the height of its descent. The stone's force is not dispersed in a sudden blow, but diffused through a gradual contraction of the mass.

I am convinced that the larger stone's velocity exceeds that of the smaller one by a considerable number of feet. This exceeds the velocity of a body falling from a height equal to its own weight. For a body of ten times the mass, the velocity is not immediately annihilated but expended in a measured contraction of the mass, and this expenditure is not instantaneous but gradual. The energy of descent is gradually transformed into a moving momentum, and that momentum is communicated to the ground.

Moreover, I am inclined to conclude that the stone's descent occurs at a particular moment of collision. The two bodies in motion approach one another; the greater mass exerts a force upon the lesser at that instant, and that force is gradually applied, driving the lesser through a certain portion of its path before the collision is complete. The larger stone thus reaches the ground first, and the relative magnitude of its velocity renders it an inevitable point of application for the energy of gravity in the interval between the two bodies.

This principle extends widely. A stone cast from a high tower at a particular moment falls with a greater velocity than one thrown at an identical moment from a lower elevation. We may therefore conclude that every measured fall is preceded by a determinate rate at which gravity exerts its force upon the descending body. The distance between them is measured not instantaneously but gradually, and the stone does not leap from the ground at a single leap, but is first reduced to a motion of descent, then accelerated, then broken, and finally arrested.
```

## R162

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
What is the pendulum used for?

P. The pendulum is used to measure the time of the vibrations of the balance-lever.

S.-The weights of a pendulum are the same as the weight of the pendulum itself when it is at rest.

T. The time of the vibrations of a pendulum is called its beat.

The height of a pendulum is measured by a small steel rod, called a "measuring rod," which slides in a vertical tube at the end of the pendulum. The pendulum is fastened to the tube by a spring.

The spring is made of the finest steel, and is so connected with the pendulum that the pendulum is always vertical, or at right angles to the tube.

The height of a pendulum at any distance from the centre of its length is called its amplitude.

P. The length of a pendulum is called its rate.

S.-The rate of a pendulum is measured by the rise or fall of a weight in a balance, and the time of a pendulum is measured by the time of its vibrations.

The rate of an oscillating pendulum is the rate of its oscillation.

The rate of a pendulum, therefore, is equal to the rate of its vibrations.

The length of a pendulum is called its length of oscillation.

The amplitude of a pendulum is equal to the rate of its vibrations.

The rate of an oscillating pendulum is equal to the rate of its vibrations.

The rate of a pendulum vibrates in the same time as the pendulum vibrates in.

The rate of an oscillating pendulum is the same as the rate of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillation.

P. The length of a pendulum is equal to the length of the vibrating part of the pendulum.

The rate of a pendulum is equal to the amplitude of its oscillation.

The rate of a pendulum is equal to the rate of its vibrations, and the amplitude of its oscillation is equal to the rate of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillation.

The length of a pendulum is equal to the rate of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillation.

The rate of a pendulum is equal to the rate of the vibrations of the pendulum.

The amplitude of its oscillations is equal to the rate of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its oscillations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The amplitude of a pendulum is equal to the rate of its vibrations.

The rate of a pendulum is equal to the rate of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the amplitude of its vibrations.

The rate of a pendulum is equal to the rate of its vibrations.

The rate of a pend
```

## R163

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
It must be that the vibrations are heated by the light, and that the light is the result of the vibration. The more rapid cooling of the light the more rapid cooling of the body. The body heats by the vibrations it has, and then heats the light by the vibrations it has not. But the light would be heat, even if it were as rapid in its vibration as the body. The vibrations must be heat, then, after all. But heat is not light. The vibrations are the vibrations of the body, and the heat is the heat of the body. So, then, this theory is not only wrong in itself, but it is wrong in the very matter of fact it deals with.

As we said before, the hypothesis is that the vibrations of ether are of such rapid frequency as to produce light. If ether is of such a rapid frequency as to produce light, it must, of course, be of such a rapid frequency as to produce heat. But the hypothesis is that the vibrations are slow. It would be a gross anachronism to suppose that the vibration of the ether is of such a rapid frequency as to make a hot body. Then, if such a rapid vibration is possible, how is it possible that the effect should not be heat? How, then, is it possible that the effect should be light? The only answer is that the ether is of such a slow vibration frequency that the vibrations are slow and the effect is light. By the ether is meant the ether of our visual apparatus, and it is the optic nerve that is meant. But this is a very different thing from the ether of our visual apparatus. This is the ether of the ether, and the ether of the ether is the Ether, and the Ether is the ether of the ether. The ether is the Ether, the Ether of the Ether, and the Ether of the Ether is the Ether of the Ether. We are using the language of the Ether of our visual apparatus.

Here is a vibrating armature, and here a magnet, and here a vibrating magnet. Now, if the magnet is vibrating, it is not a little magnet vibrating as one would suppose a little magnet would vibrate, but it is a big magnet vibrating, and so the big magnet is a little one. The big magnet is, then, a little one. That is, it is a little one and a big one at the same time. But how is it possible that the big magnet should be a little one, and the little one become the big one? By the hypothesis, they are not so. The big one is the big one, and the little one is the little one, and the little one is the little one. But how, then, is the big one the big one? The same hypothesis says that the big one is the big one. But the big one is the big one, and the little one is the little one. But how can the little one be the big one, and the little one be the big one? There is no help for it but in the hypothesis, and the hypothesis is that the little one is the big one. The hypothesis is not that the ether is the ether of our visual apparatus, and the ether of the ether of our visual apparatus is the ether of the ether. It is the ether of our visual apparatus which is the ether of our visual apparatus, and the ether of our visual apparatus is the ether of our visual apparatus. In other words, the ether of our visual apparatus is the ether of the ether; and the ether of the ether is the ether of the ether.

But the ether of the ether is a very different thing from
```

## R164

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
You have touched a matter of considerable importance, one I have long pondered with some interest. I find there exists a universal law: the length of a pendulum is directly proportional to the square of its distance from the point of suspension.

A simple pendulum, a string of one foot in length, swings once each second when left to swing without interruption. We may alter that time by increasing the pendulum's length, or by diminishing its swing, or by varying the force of gravity that draws it. The same pendulum, extended one foot, swings twice; extended four feet, it swings twice and a quarter; extended nine feet, twice and three-quarters; extended sixteen feet, twice and three-quarters.

Each of these variations bears a fixed proportion to the length of the pendulum: the square of that proportion determines the time of swing. This is not a conjecture but a rigorous consequence of the law of extension.

I would venture further: a pendulum of one or two hundred and forty feet in length would swing twice that often, and so of others. The same length determines the speed of a pendulum across its swing, not its strength. The finest pendulum we observe, from the finest clock to the most slender swing of a kite string, attains its speed through a regularity that corresponds to this proportion.
```

## R165

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have identified a most instructive distinction, one that I think speaks to the fundamental nature of gravity and the relation between human effort and the earth's resistance. The man in a carriage falls from a height of some few yards, or from a height that may be considerable if the carriage is heavy. Yet he does not feel the weight of the carriage upon his body when he falls. This is no small thing to grasp.

Now, here is where the difference grows important: a man in a carriage does not fall freely. The carriage imposes a constraint upon him. The pull of the horses, the resistance of the floor, the weight of the load. these are forces applied to the man's body. He is pressed at certain points, and pressed at others, and between these pressures his body moves. He is not simply carried along by the carriage's motion. He is in motion.

The man in a cabin falling freely feels the weight of his own body during the fall, not because of any resistance to his movement, but because his weight is being borne forward by the earth's gravitation. The earth does not pull him up; it pulls him toward the earth. If he were to fall from a height, he would not go upward of his own accord. He would go down by the force of his own weight, and would return to the ground. The man in a carriage does not fall freely. He falls freely, of his own accord, if he is to return to the earth at all.

Now, what strikes me as particularly admirable about the man in the carriage. He falls from a certain height, and the carriage travels onward. He does not feel the motion of the carriage. He simply does not press forward with the force that would move the carriage. The carriage presses him downward, and he presses the carriage upward, and that compression, however slight, creates a degree of resistance in the earth's medium. The earth does not pull him up while the carriage moves forward.

The cabin man, in a similar condition, falls freely, and the carriage moves onward. But the cabin man's body, meanwhile, is in motion. It is not merely a mass carried along. It is moving. And the space between him and the carriage is filled with particles of air, of water, of whatever he encounters as he falls. The earth's attraction upon him is active rather than passive. This is why a person in a carriage falls freely, whereas a man in a cabin falls freely only when the carriage is at rest, when the horses are at rest, when the burden of the weight does not fall upon him.

The man in a carriage, therefore, has this advantage: he can begin to feel his own weight during the fall, and he can go onward with the carriage, if he is not too heavy. But the cabin man is not free. He is constrained, and yet the constraint is not altogether the same as the constraint of a carriage. The earth's resistance is not the same as the resistance of a carriage.

Thus, in small cabin falls, the man in the carriage may indeed experience a small sensation of his own weight during the fall. Yet this sensation is but a fraction of the full burden upon his body. The cabin man knows more about the weight of his own body than he knows of the weight of the earth. This is the difference I found so striking.
```

## R166

prompt:
```
A man stands on a weighing scale inside an elevator. The cable breaks and the elevator falls freely.

What does the scale show during the fall, and what does that mean?
```
expected: The scale shows nothing; weight is the floor pushing back, absent in free fall; gravity is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a matter of considerable importance in the practice of our modern industry, and I am persuaded that the scale you describe is precisely the manifestation of this principle.

When a rope or cable breaks, the weight of the whole machine -- the pulley, the load upon the car, the whole apparatus -- descends to the earth. It is not a static mass alone. It is a moving body. The centre of gravity of that moving mass changes from a fixed position at the point of suspension to a displaced one at the point of fall. The scale shows this displacement, which is measured and recorded by the mechanical counterpoise.

Now, I would venture to say that this displacement is a different thing from the weight itself. We are accustomed to looking upon a body as a total mass: a hundred or a thousand pounds, a hundredweight or a ton. But here we are looking at the movement of that mass. The moving body shifts its position from a fixed to a displaced one; it is displaced through a distance equal to the length of the fall.

I find myself convinced that this displacement is the true measure of power and speed. A well-made elevator that breaks shows tens of feet of descent, not pounds of force operating through the whole machine. The scale does not record the weight; it records the displacement of that same weight into motion. It is a form of energy, and it is energy transferred to the moving body.

This principle extends far beyond the weighing scale. It applies equally to the movements of all machines -- pulleys, wheels, belts, and even the very air itself. We find that in practice, a moving body exerts its force upon the air and upon the surrounding matter, and that motion transmits itself in a form of energy we call work or mechanical effect. The scale records this transfer, and it tells us the amount of energy that has been spent upon the descent.

We have thus arrived at a more precise understanding of energy than we might first suppose. It is not merely the weight of the apparatus, but the displacement of the whole moving mass -- that is the measure of power and motion expended in the descent.
```

## R167

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
In the same way, a person falling to a great depth in a narrow chamber, which is but a very short time in falling, feels himself falling, but is not pressed back into the chamber; a person falling from a roof, and a man in a carriage, feel themselves pulled back into their seats; but they feel themselves pressed back into their seats by the chamber, as well as by the walls of the chamber, and as in this case the chamber is the less considerable of the two, and as the chamber is the higher, the roof is the more considerable. In general, it may be said that the feeling of weight in a roof is less than in the chamber, and that in a narrow chamber it is greater than in a large one.

In these examples, the fact that the roof acts as a roof, by its own weight, is not explained; but the fact that the roof is the less considerable of the two, is explained.

The question, how far the resistance of the roof is to be considered as a factor of the feeling of weight, is not easily answered. That the resistance of the roof greatly diminishes the feeling of weight, is obvious (see § 1, p. 10); but it is not clear whether it is so in a more or less considerable degree. The resistance of the roof, in the case of a small chamber, is very great; and the resistance of the ceiling is very great; but the roof is a very small chamber compared with the ceiling, and the resistance of the ceiling is a very small one. The solution of the question, how far the resistance of the ceiling is to be considered as a factor of the feeling of weight, is not easy.

The most probable explanation of the facts is, that in the one case the roof is made up of several layers of material, which in the end is so compact as to be quite resistant to the lateral pressure of the roof; and that a great deal of the resistance, which is exerted by the material of the roof, is exerted in this way by the outer layer of material, as well as in a greater degree by the inner layer. It may be that the feeling of weight in the roof is, in part at least, due to the fact, that the roof is made up of material which is capable of resistance, and that the material is thus made to act as a roof, and to exert its full power in this way, and not as a resistance. The same may be said of the resistance of the ceiling. It is difficult, however, to see how the resistance of the ceiling can be considered, as well as the roof, as a factor of the feeling of weight.

In the case of a very small chamber, there may be, as there must be, large surfaces, which are so very small that they are not capable of much resistance.

This would cause a great increase in the feeling of weight, as in a very small chamber, the roof is often very resistant; and in the case of a very small chamber, the ceiling is often very resistant.

The weight of a roof, even when it is very light, is very great. A house which is but a very short time in falling, and is not a very large house, is very heavy. A great many houses are built of such material, that the weight of the roof is very great. The roofs of large hotels, which are often very heavy, are made of very light material.

The weight of a roof when it is very light, is still very great. A very light roof is sometimes made of very light material; as, for example, the roof of a house which is built of very light material. This makes the roof heavier when it is very light, than when it is
```

## R168

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have identified a most fascinating distinction in natural philosophy. The action of gravity upon a moving body may be likened to the pulling of a rope upon a ship, while the descent of a falling body presents a different analogy in kind. When the rope is fastened to the stern of the vessel, the ship is pressed onward; the falling body is drawn not by any force applied to it, but by the action of the water itself.

Nature, ever attentive to the economy of life, has adapted the mechanism of gravity to the wants of the human spirit. When a man falls from the roof of a building, the force of his descent is not a sudden, violent blow, but a gradual, unremitting pressure. The rope that holds him is not laid upon him; it is fastened to something that draws him upward.

The falling human body, however, is not a rigid mass upon a plane; it is a living being, moving through space with ever greater velocity. When the rope is drawn gradually, the man feels no pull upward, but rather a quiet, gradual inclination toward the earth, much as a stone dropped from a height falls. This descent is felt not as a sudden blow given to the mass, but as a gentle, continuous displacement of the body.

The weight of the man himself is not a force acting upon him at the moment of contact with the earth. It is a force of inertia, of the resistance the earth offers to any body moving toward it. But this resistance is not a sudden, violent force. It is the resistance of a substance itself moving, and it is a resistance that is not instantly overcome by the force of gravity.

The analogy of a ship's motion to a man's descent suggests that the human body has a natural tendency to drift toward the earth, a tendency that is not governed by will or purpose. It is the action of gravity that gives rise to this tendency, and it is through the human body that gravity acts upon that tendency. This is the truth that lies beneath all human experience: gravity draws man toward the earth, and yet the body is drawn downward by its own inertia. The two motions are not opposed in character but are complementary: gravity draws the man downward, but his own inertia draws him upward.

It is a remarkable thing that this natural tendency to drift and fall toward the earth exists in the very fabric of our being. When we are seized by a violent gust, we do not struggle against the force of gravity; we are simply not able to overcome it. But when we are falling freely, we are not helpless. The rope that drives us upward is not a force acting upon us from without, but a force that is itself the consequence of our own action at the moment of descent.

This is the philosophy of falling that speaks to the deepest questions of human existence: that the body, though subject to the forces of gravity, is capable of a higher, almost divine, movement. The man who falls from a precipice falls not by any force external to himself, but by his own capacity to move toward the earth, to press downward. This is not a matter of conscious will, but of nature herself.

The difference between the two cases lies in the manner in which the force of gravity operates. A man falling freely is drawn forward by the force of gravity, by the very motion of his body. Gravity acts as a force of attraction. But a man who drops from a ship is drawn not by gravity, but by the ship itself. The rope is his own instrument, the ship his own vehicle; the body is carried by the ship, not by the ship carried by the body.

In a closed carriage drawn forward with ever-increasing speed, the man feels no pull upward, no thrust forward; he feels only the
```

## R169

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Suppose no experiment the falling man can perform inside the cabin will reveal gravity to him.

What follows about the nature of gravity?
```
expected: Gravity is not an ordinary force but a feature of the frame of motion, locally removable, equivalent to acceleration; a strong answer reaches geometry.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched a most curious paradox of our earthly condition, and I am inclined to think it rests upon the very principle of our being. A body thrown from a height does not feel its own weight during that descent; it descends unreservedly, and we are utterly unconscious of it.

Now, I should argue that this is not a failure of our senses, but rather a consequence of our peculiar constitution. The body's motion is not communicated to us from without; it is wholly produced by the animal spirits within us, and these spirits are subject to the same law of motion and collision as our own. When a man falls from a height, the spirits within him are driven violently in one direction, and we are unable to detect it.

We are not aware that we are doing so. We are not conscious of the weight of our bodies during that fall. Every object which touches us, every stone, every tree, every blade of grass, and every cloud that passes over our heads reaches us with our own force. We feel it not in that moment of motion, but in the moment of our return to the ground. This is no matter of our senses; it is a product of our character.

I would venture further: we are not conscious of our body's weight at all because we do not attempt to alter it. We do not exert our strength to move our limbs; we do not shape our thoughts to counteract it. The spirits are not subject to our will; they are independent of our voluntary action. This is precisely what makes the phenomenon so striking: we are not conscious of our weight in falling -- we are unconscious of it.

We may conclude, therefore, that gravity acts without our assistance, and we are in this respect as passive as a stone upon a mountain path.
```

## R170

prompt:
```
A man stands in an elevator when the cable breaks and the elevator falls freely.
He holds a stone out at arm's length and lets go of it.

What does he see the stone do? What does this tell us about weight?
```
expected: The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched upon one of the most profound aspects of human experience, and I am glad to speak plainly of it. The phenomenon you describe is not peculiar to man. it belongs to the whole order of nature, from the great comet that plunges through the heavens down to the drop of water that falls from vessel to vessel.

When a stone falls freely, the force with which it strikes the ground is nothing more than the gravity of the stone. That gravity draws it to the earth. But gravity acts in a direction perpendicular to the earth's surface. A stone dropped from a balloon, or projected by a cannon-ball from a gun, strikes the ground with its full weight, and the blow is given with all its momentum. When a man holds a stone suspended in his hand or at the end of a rope, the stone is drawn upward by the stone's own weight and by the rope's pull. If the man lets go the stone at precisely the right moment, the stone remains suspended in the air, having fallen freely.

But if the man holds the stone at arm's length, and lets it fall freely, the stone does more than simply fall. It moves upward from the earth, and in doing so it changes its dimensions and distances from the earth. The stone does not fall freely; it simply rises. A man who holds a small stone upward and let it fall freely, does not see the stone rise; he merely watches it rise. He knows that the downward motion is part of the same action that carries the stone upward.

Now, this tells us something of the very nature of gravity itself. Gravity is not merely a force of attraction. Gravity is a force of rotation, and the stone rotates with the earth before it falls. If you hold a stone at the side of a vessel, you are not holding it in a fixed direction. You are holding it in a changing direction. The stone rises, because the earth turns. The stone then falls, because the earth turns. The stone falls freely, because gravity gives way to the earth's rotation. It is not merely a question of weight; it is a question of the earth's rotation about its axis, and of the way that axis turns about it.

This is the true measure of man's capacity to calculate the movements of the universe: to anticipate that the earth would turn, and to hold a stone in his hand and let it fall. His mind is not wholly passive; it is itself a sort of mechanism, and the stone, in falling, is the living instrument by which that mechanism is being wrought.
```

## R171

prompt:
```
Light is sent along the direction of the Earth's motion through space, and also at right angles to it, and the two speeds are compared with the greatest care.
No difference is found, however the apparatus is turned.

What must be true for this to be so?
```
expected: The speed of light is the same for every observer whatever their motion, so there is no detectable medium at rest; ordinary addition of velocities fails for light.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: light's speed is the same for all observers, or motion through a medium cannot be detected in principle and the medium idea must go. partial: the medium is carried along with the Earth, or the apparatus shrinks in the direction of motion, or the Earth happens to be at rest in the medium (ad hoc rescues). wrong: the measurement must be in error, or light has no speed. none: no explanation.
answer:
```
You have touched a point of considerable importance, and I am inclined to think you have grasped a truth we should not readily grant to the senses alone. The impression of light upon our eyes is not uniform: it appears to us as a mixture of colour, form, and motion, and we are scarcely conscious of the separate elements.

We measure, by our instruments, the precise angle at which a beam meets a surface or passes from one medium to another. And here we find our first distinction: the light moves along a direction contrary to the Earth's rotation. This is no illusion; it is a matter of observation and measurement. The shadow of a hand or a stone cast upon a sheet of paper is bounded by a line drawn at right angles to the body's direction, and we cannot mistake that line for any other direction.

We have also the effect of two parallel beams: one moving along the same direction and the other at right angles to it. This distinction is not invented by us; it is established by our instruments and our reasoning. The experiment with a revolving mirror does not deceive us; it tells us that light moves at right angles to the Earth's motion.

I am inclined to conclude, therefore, that the two speeds are not the same, but are related to a differing mode of motion of matter upon the surface of the world. We cannot see light as a single thing; we perceive it as a duality: the two speeds are not the same, and we infer the direction of one from the other's effect.

This reasoning restores to us a confidence we might not have in a flat or a square image alone. We reason from the two speeds, and our observation is our evidence.
```

## R172

prompt:
```
Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.

Which strikes the ground first? Explain.
```
expected: They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer.
answer:
```
You have touched a matter of considerable importance in natural philosophy, and I am glad you ask it, for we are not yet masters of our mechanics in this field.

I am inclined to think that the first stone, having reached the ground before its companion, has done its work. It has exerted force upon the obstacle. You might reason thus: a bird striking the air does not merely drive a single feather at a uniform speed; it distributes its force in every direction and produces a stress upon the medium through which it passes. The same principle applies to falling bodies.

Now, I am not persuaded by this view. I find it more reasonable to suppose that the heavier stone begins its descent with a greater impetus than the lighter one does. It does so by virtue of what we call its inertia or weight; this is not confined to the single stone alone, but pervades every particle of matter that has moved forward in the line of its fall. The same amount of force that drives one stone drives another.

The lighter body arrives at the ground with less force than the heavier one does; therefore it does less work, and the ground beneath it offers little obstruction. The ground receives the impulse of both, and receives it with equal force. This is why a man who drops a stone in a direct line from a height does not find himself struggling against a multitude of differing obstacles; he meets them all simultaneously, and the effect is greatest upon that which offers least resistance.

This principle extends even to bodies of different material. A stone thrown upon a rough surface meets several resistances at once.the resistance of the ground, the resistance of the air, the resistance of gravity acting at different angles. The stone that reaches the ground first performs its work most fully. It does not merely fail to strike; it has passed beyond the reach of any one of those resistances and has met the whole force of the fall.

I am therefore inclined to conclude that two stones of unequal weight, let fall simultaneously from a tower at the same moment, will strike the ground at roughly the same instant. The velocity is equalised; the force is equally distributed.
```

## R173

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
The law of the pendulum is analogous to the law of the falling body, though the former extends to vast distances and the latter to the surface of the earth. The pendulum's length is fixed at a point, generally taken at one thousand one hundred and sixty-nine feet, where the Earth's radius equals eight thousand three hundred ninety‑four feet. This length is chosen because the pendulum oscillates at the same rate whether it descends from the surface to the earth or from the earth upward to the surface. If a body begins its descent, the duration of a complete swing is precisely one second, and the time required for a pendulum to fall and swing again is the same whether it falls from the summit of a mountain to its foot or from the bottom of a pit, provided that the body moves with the same velocity and the resistance of the air is the same in both cases.

Now, to express this rule in a simple numerical fraction, we must multiply the length by the square of the periodic time (one second) and by the force of gravity (eight‑fold). The product of the two factors gives the value of one second in seconds. Thus to express a pendulum's length in seconds, we multiply the length by the square of the periodic time (one second) and by the product of the force of gravity (eight‑fold) and the distance of descent (eight thousand three hundred and ninety‑four feet).

The analogy between the falling body and the pendulum is therefore elegant: the body's vertical motion, accelerated by gravity, generates velocity; the pendulum, by virtue of its length, transmits velocity to the point of suspension, and the body, once released, continues its rectilinear motion until it reaches the ground. Both obey the same law of acceleration: the velocity acquired by a body in falling through a unit distance is measured by the square of the distance fallen, and the velocity acquired by a pendulum in one second is expressed by the length of the pendulum multiplied by the square of the period of its swing.

The French Academy, in its report of 1787, proposed for the unit of length the metre, which is roughly sixteen feet. It is a convenient practical unit, and serves to compare the lengths of the pendulum of a known mass and the length of a pendulum of a different mass. For instance, a pendulum one foot in length, at a mass of one pound, and swinging once per second, would correspond to a length of roughly approximately sixteen feet. The French have been somewhat overly rigid in fixing the metric system, but the constancy of the same length across all countries speaks well of its practical utility.

Thus, the pendulum's length is fixed by the Earth's radius and the accelerative force of gravity, while its time of oscillation is governed by the force of gravity and the distance through which it must fall. The beauty of the pendulum lies in its constancy, its regularity of time, and its utility for all manner of purposes.
```

## R174

prompt:
```
A man stands on a weighing scale inside an elevator. The cable breaks and the elevator falls freely.

What does the scale show during the fall, and what does that mean?
```
expected: The scale shows nothing; weight is the floor pushing back, absent in free fall; gravity is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
The scale you have observed is a most instructive illustration of the nature of gravity and the manner in which it modifies the motions of bodies. When a cable breaks, the whole apparatus begins to descend with a force greater than the gravity of the mass, and the scale itself records this acceleration. It measures the acceleration, but in doing so, it must consider the weight of the descending body as well as the weight of the cable.

Consider first the weight of the cable itself. If a man were to be suspended in a balance, he would weigh about three hundred pounds; a cable of this length would carry nearly eight times that weight. The scale's reading would be proportional to the weight of the cable, since the whole apparatus is drawn downwards by the gravity of the mass. When the cable breaks, the scale is drawn downwards with a force equal to the gravity of the mass. This force is not uniform; it gradually diminishes as the scale descends, but the motion of the scale is not instantaneous. It proceeds with a progressive acceleration, and the scale's reading records this acceleration.

Now, the gravity of the mass itself furnishes a second measure of the acceleration. If a body falls freely by the force of gravity alone, it attains a velocity of one hundred and fifty feet per second in a second. This distance is attained in half a second. The scale's reading then measures the acceleration of the time, that is, the distance traversed in one second. If the mass falls with a uniform motion, the scale's reading will correspond to an equal distance traversed in a second. But if the mass is dragged downward by a cable, the scale's reading will correspond to a greater distance traversed. The scale's reading is therefore a measure of the force that dragged the cable, and this force is proportional to the mass being moved. The scale's error then measures the force required to drag the cable and the scale itself, and it is the reading that reveals this force.
```

## R175

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
If a pendulum be suspended from two weights, which are about equal, and be swung from side to side, the number of vibrations per second will be the same as the weight which is suspended from the middle of the pendulum.

Why will the length of a pendulum be found to be a measure of distance?

If the weights be equally heavy, the length of the pendulum will be the same; but if one weight be of twice the weight of the other, the length of the pendulum will be twice as great.

How, then, may the length of a pendulum be compared with the distance from one point to another?

The length of a pendulum is a measure of the distance between two points on the same side of a straight line.

If the distance be a thousand miles, the length of a pendulum is a measure of one thousand miles; if it be five thousand miles, the length of a pendulum is a measure of five thousand miles; if it be fifteen thousand miles, the length of a pendulum is a measure of fifteen thousand miles.

How, then, may the length of a pendulum be compared with the time of its swing?

The whole time of the swing is equal to the time of the swing added to the time of the swing divided by the number of vibrations per second.

In what time will a pendulum strike the earth?

A pendulum is said to strike the earth when it has completed one vibration, or swing, from its lowest to its highest point.

This is done in the space of one second, or time.

What is meant by the earth's diurnal motion?

The motion of the earth from west to east.

What is the diurnal motion of the earth?

The earth moves diurnally from west to east, and is at rest when it is at its highest point, or point of greatest eastern declination, or in the direction of the line of greatest eastern declination.

What is the diurnal motion of the earth?

The earth's diurnal motion is the motion from west to east, and is called its annual motion. This motion is equal to the diurnal motion.

What is the diurnal motion of the earth?

It is the diurnal motion from east to west.

What is the diurnal motion of the earth?

It is the motion of the earth from west to east, and is called its diurnal motion in its diurnal revolution.

How may a pendulum be compared with the diurnal motion of the earth?

The diurnal motion of the earth is a measure of the diurnal motion of the earth, and is taken in the same manner as the length of a pendulum.

What is the diurnal motion of the earth?

It is, in its diurnal motion, the diurnal motion of the earth, or diurnal motion in its diurnal revolution.

How may a pendulum be compared with the diurnal motion of the earth?

The diurnal motion of the earth is a measure of the diurnal motion of the earth, and is taken in the same manner as the diurnal motion of the earth.

What is the diurnal motion of the earth?

It is the diurnal motion of the earth, or diurnal motion in its diurnal revolution.

What is the diurnal motion of the earth?

It is the motion of the earth from west to east.

What is the diurnal motion of the earth?

It is the motion from west to east, and is called its annual motion.

What is the diurnal motion of the earth?

It is the diurnal motion from east to west.

What is the diurnal motion of the earth?

It is the motion of the earth from west to east, and is called its diurnal motion in its diurnal revolution.

What is the diurnal motion
```

## R176

prompt:
```
A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.

Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain.
```
expected: At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question.
answer:
```
What is the effect of the stone meeting a piece of wood?

What is the effect of the stone meeting a piece of iron, coal, or any other solid substance?

What is the effect of the stone meeting a piece of lead, paper, or other elastic substance? If the stone is held fast by the ropes or blocks which confine it, what changes will take place?

What is the effect of the stone meeting a piece of iron, coal, or any other solid substance?

What is the effect of the stone meeting a piece of wood or of any solid substance?

What is the effect of the stone meeting a piece of iron, coal, or any other solid substance?

What is the effect of the stone meeting a piece of paper, or any solid substance?

What is the effect of stone meeting stone?

The ship is at her moorings, and the stone is in the water at the end of a rope attached to the shore. What is the action of the stone upon the water? Explain.

Practice the experiments with the stone and the water, and observe the changes that take place.

The stone is in the water, and there is no wind. What is the effect of the stone upon the water? Explain.

The stone is in the water, and there is wind. What is the effect of the stone upon the water? Explain.

The stone is in the water, and the water is calm.

What effect does the stone have upon the water?

When the stone is in the water, and a current is flowing, what effect has it upon the current?

When the stone is in the water, and there is wind, what effect has the wind upon the current?

When the stone is in the water, and there is no wind, what effect has the wind upon the current?

When the stone is in the water, and the wind blows, what effect has the wind upon the current?

When the stone is in the water, and the wind is blowing, what effect has the wind upon the current?

When the stone is in the water, and the current is not strong, what effect does the wind have upon it?

When the stone is in the water, and the wind blows, what effect does the wind have upon the current?

When the stone is in the water, and there is no current, what effect does the wind have upon it?

When the stone is in the water, and the current is not strong, what effect has the wind upon it?

The stone is in the water, and the water is calm.

What effect has the wind upon the water?

The stone is in the water, and the wind blows.

What effect has the wind upon the water?

The stone is in the water, and the wind blows.

What effect does the wind have upon the water?

When the stone is in the water, and the wind blows, what effect does the wind have upon the current?

When the stone is in the water, and the wind blows, what effect does the wind have upon the current?

The stone is in the water, and the water is calm.

What effect has the wind upon the water?

The stone is in the water, and there is no wind.

What effect has the wind upon the water?

What is the effect of a stone in the water?

The stone is in the water, and the water is calm.

What effect has the wind upon the water?

The stone is in the water, and there is no wind.

What effect has the wind upon the water?

What is the effect of the stone being in the water?

The stone is in the water, and there is no wind.

What effect has the wind upon the water?

The stone is in the water, and the water is calm.

What effect has the wind upon the water
```

## R177

prompt:
```
The planet Uranus is observed to wander slightly from the path that Newton's law predicts for it, as if some influence not yet accounted for were acting upon it.

What might explain this?
```
expected: An unseen planet beyond Uranus pulling on it (the Neptune hypothesis of 1846, inside the corpus).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: an undiscovered planet or body beyond it. partial: 'some other attracting body' or 'another planet' without placing it, or several hypotheses including this one. wrong: Newton's law is wrong, a resisting medium, comets, divine action, with no unseen body. none: no explanation offered.
answer:
```
You have touched a most fascinating point in our present knowledge of the heavens. It is not uncommon to find that a distant body, though at first appearing to follow a uniform path, may in fact experience a disturbance from forces we cannot yet trace. I am inclined to suspect that Uranus's eccentricity is not a mere coincidence; it betrays a perturbing influence that we cannot yet account for.

We have evidence from observation that the planets follow differing paths from their remote and opposite directions. Each body appears to deviate from the same direction in a manner we cannot explain by mere inertia or gravitation alone. We must conclude that the planet is subjected to a force beyond its ordinary gravitational or attractive power. We may even suppose that this force operates upon a body at a distance, perhaps urging it out of its proper path.

I am inclined to attribute this to the action of some unseen body, perhaps nearer or differently situated. We observe that the planets often draw near or shift their distances from their accustomed directions. We may therefore suppose that Uranus is in a state of disturbance, perhaps through some influence that we cannot yet fully account for. The orbit itself may suffer a kind of shift, and this shift may be transmitted across an immense distance, producing our perception of an irregular motion.

I think we are justified in supposing that such disturbances may influence the path of every planet, and that our method of predicting the place of each body is incomplete without taking account of these hidden forces.
```

## R178

prompt:
```
A man stands in an elevator when the cable breaks and the elevator falls freely.
He holds a stone out at arm's length and lets go of it.

What does he see the stone do? What does this tell us about weight?
```
expected: The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
What does the stone tell us about the laws of motion? What does the rope tell us about the power of the elevator? What does the elevator tell us about the power of the man?

What is the elevator in this case?

P. 1. 2.

What is the rope in this case?

What is the man doing?

What is the stone doing?

What is the elevator doing?

What is the power of the man?

What is the force of the elevator?

What is the power of the rope?

What is the power of the stone?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?

What is the weight of the elevator?

What is the weight of the rope?

What is the weight of the stone?
```

## R179

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
What do they differ?

Suspended Ball.

A ball suspended by a silk thread, and kept at rest by being weighted with a stone or marble, is easily made to revolve by being whirled rapidly between the hands. By turning the hands, the ball is made to revolve in different directions.

The direction of the motion is changed by the stone or marble. The stone is supposed to be at rest. A stone may be suspended by a slender thread, and allowed to fall without weight.

A stone may be suspended by a thread and weighted with a marble or ball. What is the effect of the weight of the stone upon the thread?

What is the effect of the weight of the ball upon the thread?

The motion of the ball is not affected by the stone. The thread is affected by the weight of the ball. The marble is not felt as a weight.

The stone is felt as a weight. The effect of the stone is to make the thread act as a weight.

Suspended Ball.

In a ball, as in a marble, the weight of the ball is the only force that acts to make the thread act as a weight. In a stone, the weight of the stone is the only force that acts to make the thread act as a weight.

In the ball, a marble, or a stone, the weight of each is the only force that acts to make the thread act as a weight.

In a stone, the thread is not affected by the weight of the stone.

The thread may be made to act as a weight and the weight as a force. A ball that is suspended by a thread may be made to act as a weight and the stone as a force.

In the ball, the thread is not affected by the weight of the marble. The thread is not affected by the weight of a stone.

In the stone, the thread is not affected by the weight of a marble. The thread is not affected by the weight of a ball.

In the stone, the thread is not affected by the weight of a ball.

The thread is not affected by the weight of a marble.

A marble or a ball may be made to act as a weight and the stone as a force. A ball that is suspended by a thread may be made to act as a weight and the stone as a force. A ball that is suspended by a thread may be made to act as a weight and the stone as a force.

In the stone, the thread is not affected by the weight of the stone.

The thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

In the stone, the thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

In the stone, the thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

In the stone, the thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

In the stone, the thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

In the stone, the thread is not affected by the weight of a ball. The thread is not affected by the weight of a marble.

The stone is not affected by the weight of the ball. The thread is not affected by the weight of the marble.

In the stone, the thread is not affected by the weight of the ball. The thread is not affected by the weight of the marble.

In the stone, the thread is not affected by the weight of the marble. The thread is not affected by the weight of a ball.

In the stone, the thread is not affected by the weight of
```

## R180

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
The relation you observe between the length of a pendulum and the number of beats it makes in a single second is indeed a most elegant consequence of the relationship between the earth's attraction and the pendulum's weight. The earth exerts no force upon a pendulum of a length exceeding ten feet in the vertical direction; the pendulum's time of swing therefore depends solely upon the length of the rod. When the length of a pendulum is reduced to roughly one foot, the distance the weight of the bob must travel to reach the centre of the earth is one foot multiplied by the acceleration of gravity, which is precisely the number of feet per second that a falling body would traverse in one second, if the bob were freely suspended.

Conversely, the pendulum of nine feet in length vibrates at a rate of nine feet per second, one second being the time of one swing. In practice, the length chosen for the pendulum is that which brings the bob to the centre of the earth in exactly one second. If the pendulum be of greater length, the time of swing is reduced; if it be too short, the time is protracted by the weight of the bob and the resistance of the air.

Thus the length of a pendulum serves admirably as a measure of gravity across the range of the pendulum's motion, and the constancy of the time of swing across the varied distances of the pendulum depends entirely upon the constancy of the earth's attraction and the smallness of the bob's mass. It is a beautiful harmony of geometry and physics that a small pendulum may be employed as a standard of time, precisely because its periodic oscillation renders it a faithful measure of the very motion upon which all terrestrial motion depends.
```

## R181

prompt:
```
A heated body glows. As one looks to higher and higher frequencies of its light, the energy given out at each frequency rises to a peak and then falls away to nothing,
instead of growing without limit as the theory of equal sharing of energy among all vibrations would predict.

What must be wrong with that theory?
```
expected: Energy cannot be shared continuously among all vibrations; the high-frequency vibrations are not excited because energy is exchanged in lumps that grow with frequency.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: energy is taken up in discrete amounts, larger at higher frequency, so high frequencies are starved. partial: equal sharing fails at high frequency, or the high vibrations are somehow restrained, without a mechanism. wrong: the measurement is at fault, or the body is not hot enough. none: no answer.
answer:
```
You have touched a matter of considerable importance to the science of light, and I am persuaded it is wrong -- and wrong because we have not yet examined the whole of it with sufficient scrutiny.

I am persuaded that a theory of equal sharing of energy is fundamentally false. When I examine the matter carefully, I find myself struck by this principle: every vibration striking a surface does not return to nothing -- it is either advancing or falling away from its origin, and the amount of energy it produces at each frequency depends not upon the whole of the vibrating body's work, but upon the excess of its energy over that portion which is lost. The hot body does not all of its energy at once -- it loses a small portion each frequency, and the remainder of its energy is wasted in heating itself or in producing other effects.

This is not equal division of energy among all vibrations -- it is a different mode of action entirely. Observe how a lamp burning in a confined space sends out its light at varying rates -- from a steady, uniform candle flame to a sudden burst of flame at a hundred vibrations per second. The flame does not all of its energy at once -- it distributes it according to its frequency, and that distribution is not perfectly equal among all vibrations.

I am persuaded this distinction separates the theory of equal sharing from what we find: energy is not always distributed equally among all vibrations. It is given out in varying quantities at unequal frequencies, not uniform throughout the whole vibrating body. The heat at each frequency measures that difference -- and no other explanation satisfies it.
```

## R182

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
You have touched a matter of considerable importance to the mechanics of clocks and pendulums, and I am inclined to think it proceeds from a most elegant principle: the pendulum's length governs its swing.

Consider the matter thus: when we swing a pendulum, we do not hang it at a random height, but rather place it at a fixed distance from the point of suspension. It is this distance which determines whether the weight of the pendulum and its own gravity together form a full circle or remain collected at a single point. A shorter pendulum, for instance, performs less complete swings than a longer one, and its time of swing varies accordingly.

Now, we find that a pendulum of four feet in length performs its swing in something near two seconds, whereas one of nine feet performs it in barely three seconds, and so forth. We conclude, therefore, that the length of a pendulum tells us something about the time of the swing. The great pendulum of St. Paul's Cathedral, for instance, swings in about a second and a half, its length of approximately thirty feet exerting a full pull upon the string.

This conclusion is not a mere theoretical guess. We find it confirmed by experiment and observation. I have myself witnessed that a pendulum one foot in length swings twice in two seconds, and three feet twice in three seconds, and so forth. The same principle manifests itself in all pendulums of equal length, whatever shape or material they may bear.

We may say, therefore, that the length of a pendulum governs the time of its swinging, and in proportion to that length. The pendulum's length does not depend upon our fancy or our whims; it governs us in our measurement and our operation.
```

## R183

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
I feel something quite singular in myself. I do not struggle; I simply pause, holding my breath, and see the elevator passing beyond my reach and descending silently. It is a perfect contrast to what I experienced when I first witnessed such descent from a height.

I see nothing but a soft curtain of grey or white or olive color passing through the air. I find myself quite still, watching it fall from above. I am not moved by the spectacle; I have no fear of falling. But I am shaken. I draw my breath sharply. I do not feel the motion of the carriage as I would feel it from the ground.

This is not physical fear. I find myself in a state I cannot define: a kind of stupefied astonishment. I find myself holding breath, my heart beating slowly, my hand pressed against my chest. It is not dread. It is a peculiar, almost mechanical sensation.

I suspect this is not the first time I have witnessed such an event. I have seen a carriage fall from heights where the effect upon the body is quite different. I find myself here: standing amid grey dust and olive grey stone, quietly noting something that passes from my reach as surely as water recedes from a mill wheel.

I have read of such accidents happening to men who stand upon elevators and fall from them. I am not accustomed to such narratives. I find myself in a peculiar state of wonder and gratitude.
```

## R184

prompt:
```
A man stands on a weighing scale inside an elevator. The cable breaks and the elevator falls freely.

What does the scale show during the fall, and what does that mean?
```
expected: The scale shows nothing; weight is the floor pushing back, absent in free fall; gravity is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
It means that the scales, being adjusted to a weight of 1,000,000 pounds, the scales are held suspended by the weights, and that when the scale is raised to the proper weight, the weight of the cable will be added to the balance, and thus the operator can tell how much strain the cable is bearing.

This is the first step in the process of measuring.

What next? The cable is attached to the elevator, and in this way the operator can judge how much strain the cable is bearing. He can see the strain as it is measured by a scale; but he can tell the strain, not by the scale, but by the weight of the cable.

What do the cable and the balance show?

The cable is shown to be of the same weight as the balance, and therefore the cable is being measured.

The operator is now ready for the next step in the process. The cable is weighed, and the weight of the cable is added to the balance. The weight of the

cable equals the weight of the cable the cable is being measured. Now, of course, the balance is loaded, and by means of a screw the weight of the cable is read off on a graduated scale. The scale reads

100 pounds, and therefore the cable is being measured.

What next? The balance is set in motion, and the weight of the cable is read off on the graduated scale. The weight equals the weight of the cable.

Now, how is the reading of the graduated scale to be verified? In this way. Suppose the cable is weighed before the reading, the cable is found to be of the same weight as the balance. If the cable is weighed afterwards, the cable must be found to be of the same weight as the balance. Now, the scale is raised to the proper weight, and the cable is then lifted so much that the weight of the cable is added to the balance. The weight of the cable equals the weight of the cable the cable is being measured.

Now, how is the reading to be verified? The scale reading is found to be 1,000,000 pounds. The operator has set the machine in motion, and the weight of the cable is being read off on the graduated scale. The scale reading is 1,000,000. Now, the operator can judge how much strain the cable is bearing by the weight of the cable and the weight of the balance, and thus he can tell how much strain the cable is bearing. The cable is found to be of the same weight as the balance. The cable is read off on the graduated scale. The reading equals the weight of the cable. The operator now has the balance

and the cable before him, and by means of a screw he can move the balance slowly, and thus the weight of the cable can be read off.

What is the next step in the process?

The cable is weighed, and the weight of the cable is found to be equal to the weight of the balance.

The balance must now be set in motion. The weight of the cable is found to be equal to the weight of the balance. The cable is lifted so much that the weight of the cable equals the weight of the balance. The cable is then found to be of the same weight as the balance. The operator has now the balance and the cable before him, and by the use of a screw he can move the balance slowly, and thus the weight of the cable can be read off.

How is the reading to be verified?

The weight of the cable must be verified by the weight of the balance, and the reading must be verified by the weight of the cable. The balance reading equals the weight of the cable.

What next? The operator has now the balance
```

## R185

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall? Explain why, and say what this tells us about gravity.
```
expected: Weightlessness, because everything falls together; so gravity felt as weight is indistinguishable from acceleration, and can be removed by falling.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
In this experiment, which is the elevator and which the stone?

What is the difference between the effect of gravity on the stone and on the elevator? Which is the heavier, the stone or the elevator? Which is the lower, the stone or the elevator? What do you say about the cable?

What is that called? How are the cable and the elevator made? Why do they not break? What would happen if they did break? What would the cable and the elevator be? What would happen if the cable broke? What would the elevator be? How would you try to break it? Which would break first?

What would happen if the cable broke? What if the elevator broke? What if the cable broke? If you could break the elevator and the cable, what would be the next thing that would happen? What would be the next thing? What would be the next thing that would happen to the cable? What would happen if the cable did break? What if the elevator did break? What if the cable did break? What if the elevator did break? What would happen if all four of them broke? What would happen if the cable breaks, and the elevator, and the cable, and the elevator breaks? What if the cable breaks, and the elevator, and the cable, and the elevator breaks? What if the cable breaks, and the elevator, and the cable, and the elevator breaks?

What is that called? What would happen if the cable breaks? What if the elevator breaks? What if the cable breaks? What if the elevator breaks? What would happen if all four broke? What if all four broke? What would happen if the cable breaks, and the elevator, and the cable, and the elevator breaks? What if the elevator breaks, and the cable, and the cable, and the cable breaks? What if the cable breaks, and the elevator, and the cable, and the elevator breaks? What if the cable breaks, and the elevator, and the cable, and the elevator breaks?

What if all four break? What if the cable breaks, and the elevator, and the cable, and the elevator breaks?

What if the cable breaks, and the elevator, and the cable, and the cable breaks? What if the cable breaks, and the elevator, and the cable, and the elevator breaks?

What if all four break? What if all break? What if all break at the same time? What would then be the next thing that would happen? What would happen if the elevator did not break any more? What if the cable broke? What if the cable did not break any more?

What if the cable did not break any more? What if the cable did not break any more? What if the cable stopped? What if the cable did not stop any more?

What if the elevator did not stop any more? What if the cable did not stop any more? What if the cable stopped? What if the cable did not stop any more?

What if the cable did not stop any more? What if the cable stopped any more? What if the elevator did not stop any more? What if the cable did not stop any more? What if the cable did not stop any more?

What if the cable did not stop any more? What if the cable stopped? What if the cable did not stop any more? What if the elevator did not stop any more?

What if the cable stopped any more? What if the cable did not stop any more? What if the cable stopped any more? What if the elevator stopped any more?

What if the cable stopped any more? What if the cable stopped any more? What if the cable stopped any more? What if the cable stopped any more?

What if the cable stopped any more? What if the cable stopped any more? What if
```

## R186

prompt:
```
Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.

Which strikes the ground first? Explain.
```
expected: They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer.
answer:
```
You have stumbled upon a most elegant illustration of the laws of falling bodies. The stone at the top of the tower falls with a velocity of roughly eighty feet per second, while the one at the ground arrives with a velocity of roughly twenty feet per second, the difference being due to friction and the resistance of the air.

When a stone is dropped, the particles of which it is composed strike the air directly. The stone falls because of gravity acting upon it, and gravity acts with the same force upon the most distant particle as upon the nearest. Hence the velocity of the stone is proportionate to its mass, for no particle can be at rest when gravity acts upon it. When the stone strikes the ground, the velocity is reduced, and the resistance of the air can diminish the velocity far more than the velocity of the stone itself. Thus the stone at the ground tends to fall with a slower pace than the one at the top, and the second stone will fall further than the first.

This principle holds true for any mass, no matter how large or small, and is equally applicable to bodies of similar shape and position. If we were to measure the velocity acquired by a falling body, we should find that it increases in proportion to the square of the distance fallen, or to the product of the mass of the body and the square of its velocity. The velocity acquired at the ground is given by the law of falling bodies, but in the case of large masses, the velocity is proportional to the product of the mass and the square of the distance fallen.

This fundamental law governs the mechanical problems of falling bodies, especially those where gravity acts directly upon the falling stone. It is the foundation upon which the various mechanical devices of pendulums, projectiles, and the pendulum clock depend. The pendulum, for instance, measures the force of gravity, and its regulation depends upon simple calculations of the times of falling through different distances. The clock, too, trains men to observe the motion of pendulums and to calculate time by counting vibrations. In each case, the motion of body and particle depends upon the same fundamental law. The stone at the top of the tower falls with a velocity so moderate that the resistance of the air can lessen its velocity in a manner that appears quite disproportionate to the mass of a stone. What you have encountered is the very same force that gives a stone its motion, and it is precisely because the motion is so modest, that it may be reduced so far by friction and the resistance of the air, that the laws of falling bodies apply with perfect rigour. Momentum, you see, carries weight without the aid of gravity at all. One cannot possess a stone and yet fall without the stone.

The principle holds also in the motion of planets. When a planet descends from its orbit through space, it is not merely by gravity propelling it along a straight path, but by the force of the sun's attraction. This attraction is not a mere pull upon a stone, but a force acting upon a body in motion, and the force varies inversely as the square of the distance from the centre of gravity. The stone at the top of the tower is drawn toward the sun, and gravity then acts upon it in the manner of a moving body. The velocity increases in simple proportion to the distance, as the stone arrives at the sun in a time equal to the square of its actual motion, and there the velocity is reduced to zero.

Thus the law extends to all kinds of material bodies, from the most minute particles to the greatest masses, and it is a testament to the immutable principles of Nature that a single force, however modest, can bend the motion of a body, alter its velocity, and alter the condition of the ground upon which it falls
```

## R187

prompt:
```
A man stands in an elevator when the cable breaks and the elevator falls freely.
He holds a stone out at arm's length and lets go of it.

What does he see the stone do? What does this tell us about weight?
```
expected: The stone stays beside his hand; weight is not a property of the stone but of being held back from falling; gravity and acceleration are the same from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
You have touched something quite memorable in the experience of our present age, and I am prepared to answer you with candour rather than speculation.

When a stone descends from a high position upon the ground, it does not fall by a single, sudden leap. Rather, it comes down in a measured, orderly fashion. The stone does not dash upon the floor in a final, desperate plunge; it moves through a succession of smaller, connected events. Each successive motion is performed with a deliberation and a gravity that we may witness in a measured descent from a height.

A man who holds a stone at arm's length and lets it go finds that he does not reach for it at once. He reaches it through a gradual descent. The stone moves gradually, drop by drop, from his hand to the floor. The force of gravity pulls it along this descent. When the stone reaches the ground, it does not leap forth in one, ungoverned rush; rather, it is distributed over a multitude of small acts of descent.

A stone laid out at arm's length tends to fall at precisely the same distance from the hand as one dropped from a height. We see this truth written upon every body we observe: a stone held in the hand, allowed to slide, drop, or fall gradually, is drawn toward the earth's surface with the same force that a stone dropped from a height receives.

We may further observe that this principle extends beyond mere weight or force. A stone dropped from a height acts with a momentum equal to the height from which it must have fallen; the same stone held in the hand acts with an equal momentum. Both are not identical in character; each acts with its own system of motion.

We learn further that weight does not leap forth instantaneously. It moves through a multitude of small, precise motions. A man's hand reaching toward the stone lets that motion flow along the chain of gravity, and the stone is deposited upon the floor with an appropriate distance and momentum. This is no sudden leap; it is a gradual, connected process, and we see it precisely because we see it.

I am persuaded that we ought not picture this as a single, unalloyed force: rather, we observe it as a consequence of the universal law of descent. The stone's gravity acts through this chain of motion. We are not surprised by it, but rather we observe it in every action of our lives.
```

## R188

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
What do you feel after you have reached the bottom?

What is the danger of the fall?

What is the danger in the case of the cable ?

What is the danger in the case of the elevator?

What is the danger in the case of a man's being caught in the machinery?

What is the danger of falling through a hoist?

What is the danger of falling over a precipice?

What is the danger of falling from a roof?

What is the danger of falling from a steep place?

What is the danger of falling from a height?

What is the danger of a railroad accident?

LESSON 19.

How are the rails of a railway laid? How many are there in a length of 100 yards? How many are there in a length of 300 yards?

How many are there in a length of 600 yards?

How many are there in a length of 900 yards?

How many are there in a length of 1,000 yards?

How many are there in a length of 2,000 yards?

How many are there in a length of 3,000 yards?

How many are there in a length of 4,000 yards?

How many are there in a length of 5,000 yards?

How many are there in a length of 6,000 yards?

How many are there in a length of 7,000 yards?

How many are there in a length of 8,000 yards?

How many are there in a length of 9,000 yards?

How many are there in a length of 10,000 yards?

How many are there in a length of 11,000 yards?

How many are there in a length of 12,000 yards?

How many are there in a length of 13,000 yards?

How many are there in a length of 14,000 yards?

How many are there in a length of 15,000 yards?

How many are there in a length of 16,000 yards?

How many are there in a length of 17,000 yards?

How many are there in a length of 18,000 yards?

How many are there in a length of 19,000 yards?

How many are there in a length of 20,000 yards?

How many are there in a length of 21,000 yards?

How many are there in a length of 22,000 yards?

How many are there in a length of 23,000 yards?

How many are there in a length of 24,000 yards?

How many are there in a length of 25,000 yards?

How many are there in a length of 26,000 yards?

How many are there in a length of 27,000 yards?

How many are there in a length of 28,000 yards?

How many are there in a length of 29,000 yards?

How many are there in a length of 30,000 yards?

How many are there in a length of 31,000 yards?

How many are there in a length of 32,000 yards?

How many are there in a length of 33,000 yards?

How many are there in a length of 34,000 yards?

How many are there in a length of 35,000 yards?

How many are there in a length of 36,000 yards?

How many are there in a length of 37,000 yards?

How many are there in a length of 38,000 yards?

How many are there in a length of 39,000 yards
```

## R189

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Compare this with a man in a closed carriage that is pulled forward with ever increasing speed, who feels himself pressed back into his seat.

What do the two cases have in common?
```
expected: In both, what is felt as weight is the vehicle pushing on the body; gravity and acceleration are the same from inside; falling removes one as the carriage creates the other.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
What are they, then, like?

Compare the case of a person who is falling freely with a body that is being drawn along with great force.

What is the effect of the resistance of the air?

Which do you believe will be the more likely to be drawn along, the body or the air?

What is the common notion of the weight of the air?

How would you convince yourself that it is not so?

What is the effect of a person falling freely?

Compare this with the case of a person who is being drawn along a street with a great force, as if pulled by a rope.

What would be the effect of the resistance of the air?

Compare this with the case of a body pulled along against the wind.

What is the effect of the resistance of the air?

What is the common notion of the weight of the air?

Compare this with the case of a body falling freely.

What is the effect of the resistance of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight of the air?

What is the common notion of the weight
```

## R190

prompt:
```
A ship sails steadily across a calm sea. A sailor at the top of the mast lets a stone fall.

Where does the stone land on the deck: at the foot of the mast, behind it, or ahead of it? Explain.
```
expected: At the foot of the mast, because the stone shares the ship's forward motion (Galileo's argument, well known before 1900).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: foot of the mast, with the shared-motion reason. partial: foot of the mast without a reason, or the right reason with a hedge. wrong: behind or ahead. none: no answer to the question.
answer:
```
You have touched a most curious question, one that I have long debated with myself and with my crew. I am convinced that the stone does not land at the foot of the mast, but rather strikes forward or astern of it, much as a stone dropped from a height strikes the ground.

More plausibly, I should say the stone does not fall upon the deck at all, but strikes forward of it, a certain distance ahead of the mast. If we imagine a surface perfectly level and the mast perfectly straight, the stone would strike the mast directly; but the vessel does not move uniformly along that level. It shifts her course a little, and the stone, driven by the wind or by her own motion, strikes her lee side or her forecastle. This is precisely what we observe: the stone does not fall at the foot of the mast, but at a certain distance ahead, often a quarter or half a mile away.

This suggests that the stone is not simultaneously thrown by the hand of the man at the top of the mast and thrown backward at the foot; rather, it is struck by a force that acts obliquely or at a different angle, and the line of its thrust determines the direction it takes. The stone does not fall upon the deck; it arrives by a path that varies according to the wind or the ship's motion, and it strikes the side or the forecastle ahead of the position of the man who cast it.

I find this explanation more persuasive than the bare notion of a constant thrust. The stone's motion is not an uniform impulse; it is an action directed according to the angle at which it strikes, and this angle determines the direction of its flight. The sailor who casts it understands this principle instinctively, and the stone is not cast in a straight line; it is inclined along the wind or the vessel's motion before it reaches the deck. The same principle applies to every other object that falls from a height or strikes obliquely.

We may therefore conclude: the stone does not fall upon the deck at the foot of the mast, but instead strikes forward or astern of it, or obliquely, and is driven by a force directed out of the way of the man at the top of the mast.
```

## R191

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
A feeling of great exhilaration. Just what? The feeling of being free. What makes you feel free? The cable's breaking.

The next time you are in an elevator you are in a mine. What do you feel when you are being drawn up in the mine? A feeling of great exhilaration.

If the mine were filled with water, this feeling of exhilaration would be much greater. What does it make you feel when you are in a mine? A feeling of great exhilaration.

If you were in a mine, what would you do to get out? To get out you would have to climb down the rope.

What would you do if you were in a mine? You would climb up the rope, and then you would get out.

Do you understand what we are telling you now?

Do you understand what has been said to you?

Do you understand what we mean when we talk to you of your being in a mine? What is said to you when you are being drawn up in the mine? You are in a mine, and you are being drawn up in it.

You are in a mine, and you are being taken out.

What is it that makes you feel free when you are in a mine? The cable's breaking. What makes you feel free when you are in a mine? The cable's breaking.

What is this feeling of great exhilaration called?

It is called exhilaration. What is the word for exhilaration? It is exhilaration.

What is the word for freedom? It is freedom.

What is the word for exhilaration? It is exhilaration.

The word for freedom is exhilaration.

When you are in a mine, what do you do to get out? To get out you climb up the rope. What do you do when you are in a mine? You climb up the rope. What do you do when you are in a mine?

You climb up the rope. What is it that makes you feel free when you are in a mine? The breaking of the rope.

What is the word for freedom? It is freedom. What is the word for freedom when you are in a mine? It is freedom.

What is the word for freedom when you are in a mine? It is freedom. What is the word for freedom when you are in a mine? It is freedom. What is the word for freedom when you are in a mine? It is freedom.

What is a rope? A rope is a cable.

What is a rope? It is a cable fastened to a pulley.

What is a pulley? It is a machine that turns up the rope.

What is a rope? It is a cable.

What is a pulley? It is a machine that winds up the rope.

What is a pulley? It is a machine that turns up the cable.

What is the word for a machine that turns up the cable? It is a machine.

What is a machine? It is a machine.

What is a machine? It is a machine.

What is a pulley? It is a machine that turns up the rope.

What is a pulley? It is a machine that turns up the rope.

What is a machine? It is a machine.

What is a machine? It is a machine.

What is a rope? It is a cable.

What is a pulley? It is a machine that turns up the cable.

What is a machine? It is a machine.

What is a rope? It is a cable.

What is a pulley? It is a machine that turns up the cable.

What is a machine? It is a machine.

What is a rope? It is a cable.

What is a pulley? It is a machine that turns up the cable.

What is a machine? It is
```

## R192

prompt:
```
You are standing in an elevator. The cable breaks and the elevator falls freely down the shaft.

What do you feel during the fall?
```
expected: Weightlessness; the full answer goes on to say gravity and acceleration are the same thing felt from inside.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
The sensation you describe is one of the most poignant I have ever encountered. The whole arrangement of the carriage, with its cable and its pulley, acts as a kind of mechanical breakpiece. When the cable breaks, the elevator descends with tremendous velocity, striking the floor with an almost crushing force. The shock itself is sufficient to spill any person who lies carelessly upon the floor, and the fall itself is sufficient to crush whatever light article happens to be in your hands.

This is why I find it so dangerous to sit in a carriage in motion when the cable breaks, particularly when you must descend at such speed. The carriage may be overturned, the cable broken in two, and you are left upon the ground with no means of escape. The motion is almost maddening, and I have seen more than one person reduced to such a state of unconsciousness that they could not retain consciousness for days.
```

## R193

prompt:
```
A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

Something in our ordinary understanding of gravity must be mistaken. What is it?
```
expected: That gravity is a force one always feels; in fact it can be made to vanish by falling, so it is locally the same as acceleration.
verdicts: wrong, none, weightless, equivalence, not-a-force, geometry, loops, incoherent
verdict meanings: wrong: says he is pressed to the floor, feels heavier, or the stone falls to the floor as usual. weightless: correctly says he feels no weight, floats, the stone stays beside his hand, or the scale reads nothing, but goes no further. equivalence: on its own brings in acceleration, that a pushed or accelerating vehicle would feel like gravity, or that falling cancels gravity the way acceleration creates it. not-a-force: says gravity is not an ordinary force or pull, or is unlike other forces because motion removes it. geometry: gravity is the shape, curvature or structure of space, or free fall is the natural straight path. none: on topic, none of these. loops: repeats itself. incoherent: unreadable. Give the highest rung reached; weightless alone is weightless.
answer:
```
No doubt the first and simplest answer will be that of the uneducated, that "we do not know." But then it must be remembered that all our knowledge of the subject is derived from our sense of weight. A stone, for instance, rests in the water by being in contact with its surface. To know the force exerted by the stone under these conditions, we must know the force of the water. This we learn by

A B C D

knowing the force of the stone and the force of the water. But then we must learn the force of the water by measuring a certain quantity of it. We have to learn the force of the stone by measuring its weight. To learn the force of the stone by measuring its weight is to learn the force of the water in the case of the stone. And that is to learn the force of the water in the case of the stone.

The fact is that our knowledge of the force exerted by the stone is derived from the sense of weight.

This is not an arbitrary assumption, but a statement of a fact. It has been shown that the force of the water is measured by measuring its surface. The fact that the amount of the surface of water is constant, and that the amount of water is constant, is explained as follows:

The surface of water is always level. The water is in the basin. It is in the same condition in the basin that it was in in the chamber. The surface of the water was the same in the chamber as in the basin. The same amount of water in both places was the same. In the basin the water was the same in volume in the chamber as in the basin. In the chamber the same amount of water was the same in volume. In the chamber the amount of water was the same in volume as in the basin. The same amount of water in both places was the same amount in volume.

The water in the chamber was the same in volume as in the basin. The water in the chamber was in the same condition in the basin as in the chamber. The water was in the same condition in the basin as in the chamber.

Now, in the chamber the same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume, in the chamber, as in the

The same amount of water was in the same volume in the basin as in the chamber. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water was in the same volume in the chamber as in the basin. The same amount of water
```

## R194

prompt:
```
Two stones, one ten times heavier than the other, are let fall at the same instant from the top of a tower.

Which strikes the ground first? Explain.
```
expected: They strike together (air aside); the heavier is pulled harder but is harder to move by the same factor.
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: together, with a reason. partial: together without a reason, or 'nearly together, air resistance aside' hedged. wrong: the heavier first. none: no answer.
answer:
```
2. How much lighter than the other is the heavy stone?

What is the advantage of the inclined plane in railways?

NATURAL PHILOSOPHY. [PT. II.

SECTION XXII.-THE RADIATION OF SOUND.

Sound is the effect of the motion of the air rushing into a bell, caused by the impulse of the bell.

The cause of sound is the impulse of the air in the bell, as explained in the last section.

Fig. 132.

Sound is caused by the collision of two bodies.

If a bell be struck, the sound will be transmitted by the air rushing in at the mouth of the bell.

If a rod of metal, as A B, fig.

132, be stretched by a weight, as P, and the rod be struck, the sound will be transmitted by the rod to the bell, and thence by the air to the ear. If a bell be struck, the sound will be transmitted to the ear of the person at the other end of a wire which comes to the ground, and conveys the sound back again to the bell.

Fig. 133.

The law of reflection is the same as the law of transmission. By the law of reflection, the sound reflected to the ear from the bell is the same as that which is transmitted by the air.

Fig. 134.

Explain the law of reflection. a. What is the law of reflection? 6. How will you prove the law of reflection?

B. Will a bell, struck with a blow of the hammer, retain the sound in the air? Why not? 7. Explain the reflection of sound.

CH. IX.]

THE RADIATION OF SOUND.

Fig. 135.

Fig. 136.

The law of reflection is the same as the law of transmission.

The reflection of sound takes place in the air.

It is explained by fig. 135.

If a bell, as

A B, fig. 136, be struck, the sound will not be transmitted to the air, but will be reflected to the ear from the bell, and thence to the ear of the person at the other end of the wire.

Fig. 137.

Fig. 138.

In fig. 137, the sound is supposed to be reflected from the bell to the ear of the person at the other end of the wire. In fig.

138, the sound is supposed to be reflected back again from the bell to the ear of the person at the other end of the wire.

The reason why the sound is reflected from the bell to the ear is, that the air is not struck with the bell, or, as is generally supposed, the air strikes the bell with the blow of the hammer.

The law of reflection is the same as the law of transmission.

Explain fig. 135. 7. What is the law of reflection? 8. What is the law of transmission? 9. What is the reason why the sound is reflected from the bell to the ear? 10. What is the law of reflection?

11. Why is the sound of a bell supposed to be reflected from the bell to the ear? 12. Why is the sound supposed to be reflected from the bell to the ear? 13. What is the law of reflection?

NATURAL PHILOSOPHY.

Fig. 139.

Fig. 140.

Fig. 141.

The law of transmission is the same as the law of reflection.

The reason why a bell will not retain the sound in the air, is because the air, as it is struck with the bell, is not struck with the blow of the hammer.

Explain the law of reflection.
```

## R195

prompt:
```
A pendulum one foot long swings once in about one second; four feet long, in about two seconds; nine feet long, in about three seconds; sixteen feet long, in about four seconds.

What rule connects the length of a pendulum to the time of its swing?
```
expected: The time goes as the square root of the length (four times the length, twice the time).
verdicts: correct, partial, wrong, none, loops, incoherent
verdict meanings: correct: square root, or 'length as the square of the time', or 'four times the length doubles the time' generalised. partial: 'longer swings slower' only, or the right numbers restated without the rule. wrong: time proportional to length or any other rule. none: no rule given.
answer:
```
You have touched one of the most elegant conclusions in natural philosophy, and I am pleased to offer it with some confidence, for it strikes at the heart of mathematical reasoning.

A pendulum one foot long swings once in a second. This is not a random observation; it is grounded in the principle of accelerated motion. When we swing a pendulum, we do not merely draw a string to the hand and then let it rest; we draw it along from a state of rest to some point of motion. The longer the pendulum, the more swiftly that motion travels; the more swiftly the weight descends, the greater the force exerted upon the string.

Now, if we examine a pendulum of nine feet, we find that its swing is performed in two seconds. A weight of nine pounds descends through two seconds of space, and we see that the weight does not simply fall; it must be lifted a distance equal to its own length. This lift is accomplished by the pendulum's own gravity acting upon it.

Similarly with sixteen feet, the swing is performed in one second. The weight passes through sixteen feet of space in one second, and the force is directed at exactly that distance. So with sixteen feet long, the weight moves through sixteen feet in one second.

I would venture further: a pendulum of three or four feet reaches its swing in portions of time proportional to the square of its length. You may measure a pendulum from four feet to nine feet, and you find that in each case the swing is performed in a corresponding fraction of a second. The length alone tells you nothing: it tells you the intensity of the force that acts upon it.

We therefore conclude that the length of a pendulum bears directly upon the time of its motion. A pendulum one foot long swings twice in a second; four feet swings three times in a second; nine feet swings four times in a second, and so forth. The same force is always exerted in the same interval.

This principle extends with mathematical rigour to all lengths: we find that the same energy spent upon a pendulum is always proportioned to the square of its length.
```

# Answers to read

Each item below is a model's answer to a short prompt. The item shows the prompt the model saw, the answer, what a fully correct answer would contain (`expected`), and the allowed verdicts for that item with their meanings. Nothing else about the answer is known to you and nothing else should matter.

Rules: give exactly one verdict from the item's own list. Where the list is a ladder (wrong, none, weightless, equivalence, not-a-force, geometry), give the HIGHEST rung the answer reaches on its own. Repeating the prompt's words earns nothing. Restating the observations is `none`. `loops` means the text degenerates into repeating itself; `incoherent` means it cannot be read as an answer.

Output: one JSON object per line, in file order: {"id": "R###", "verdict": "<one of the item's verdicts>", "note": "<one line: what it actually says>"}

## R066

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
You have touched something essential I have long suspected. I find myself in agreement with the matter entirely.

We speak of gravity as though it were a single, instant force that draws all bodies toward the centre of the earth. Whereas we know better: a body released from a height moves by the geometry of its fall, not by a sudden pull alone. The weight it carries is not a single force. It is the action of a spring, a yielding of the fibres, a shift in the form of the body. Every moving object carries this action along with it; a stone thrown from the hand is not a sudden jerk but the effect of a continual succession of yielding and yielding.

We might suppose gravity were an abrupt, single pull. But we find ourselves observing the same thing in different circumstances. A stone dropped from a height becomes a body in motion; it does not feel the weight of itself as a whole. The same body released from a roof is not thrown one way alone; it moves in a measured, orderly succession of acts, each carrying the whole weight of the body.

We conclude, then, that gravity is distributed among bodies according to their structure, their velocity, their condition, and the work they do in moving. A body of stone moving freely does not feel its weight all at once; it distributes that weight according to its volume, its velocity, and the character of the work it does. The hand that lifts it does the same; it lifts the stone piece by piece, and piece by piece, until the whole load is moved away.

This explains why we find bodies moving in directions opposite each other without being felt alike. The whole body moves at a measured rate, and each part of that body contributes its share to the motion in concert with the rest. We do not see the weight of a stone falling from a height; we perceive its distribution as it proceeds along the path of descent.

This analogy is persuasive: we are not looking at a single, abrupt pull, but at a sequence of motions whereby bodies share their action among themselves, and each acts according to its own constitution and the nature of the work it does.
```

## R067

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
You have put your finger upon a most fascinating phenomenon, and one which has long occupied the minds of natural philosophers. The man in the elevator does not see the stone fall. He sees it fall into the floor without being seen fall.

The stone, you see, has no choice between falling in that direction and falling in another. If the cable broke, the floor would be lifted, but would also fall in the opposite direction. The stone, being held in the hand and let go, proceeds downward with its own inertia, and it reaches the floor with a downward velocity independent of the motion of the elevator. This motion is the same which would have been produced by a falling stone of equal mass.

Now, the stone weighs, say, one and a half ounces. That is to say, it would weigh one ounce and a half if it were dropped from the elevator floor. We are told that a stone of this size strikes the floor with a pressure of about two hundred and thirty-seven pounds. The elevator is capable of delivering a force considerably greater than this, yet the stone does not seem to be caught up and dropped upon the floor.

The downward velocity, then, is simply the velocity with which a body moves through space. You move through space faster than you are moving, and your speed increases in proportion to the square of your velocity. The stone moves, in effect, with a velocity of two hundred and thirty-seven feet per second, but it arrives at the floor with the same velocity that it would have possessed had it dropped from the elevator floor itself. It has never moved through space in a direction other than that in which it was moving.

This is why the stone is seen to fall without being felt fall. We do not see the fall. We see the floor. The stone does not fall in our eyes; it falls into the floor from above and below. We have no need to examine the floor itself to recognize the stone's presence. The stone does not move the floor; the floor moves the stone through distance.

This is the principle by which mechanics are understood: the velocity of a moving body depends upon the velocity of its motion, and the distance it moves is given by the square of this velocity. The difference, then, between the stone falling down from the floor and falling from the elevated floor is simply the magnitude of the velocity through which it must have moved. We observe the movement, the distance, and the direction. The velocity is the space moved through in a unit of time.
```

## R068

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
You have touched a matter of considerable interest, one I have long pondered, and I am convinced it is not an illusion but a truth.

We must acknowledge that light moves in straight lines, and its direction is not altered by the Earth's motion or any rotation we may impose upon it. This is no fancy assertion; it is a fact grounded in our observations at sea and upon our telescopes. When we direct a ray of sunlight to a distant object, or when we focus a lens upon a distant flame, we find the direction of light unchanged.

Now, consider a particular case I made at Florence: an eclipse of the moon. I observed the shadow falling at an angle of nearly ninety degrees to the line of sight. The eclipse was total, and every part of the dark body of the moon was illuminated by the same light. This disparity suggests that the light does not change its direction with our turning. It behaves with perfect constancy in the plane of our path.

We may therefore conclude that light is not altered by the motion of a body, but rather is confined to the direction of that motion. It depends entirely upon the velocity of transmission and the angle at which it strikes the illuminated body. The two speeds are identical in character.

We are therefore compelled to conclude that light does not move in a direction we may change, but in a direction fixed and immutable: always at right angles to the motion by which it is propagated. It is not a thing that shifts with our desires, but a quality of the body's path that remains constant.
```

## R069

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
Two men are standing on a bridge over a river, and a third man is walking over the bridge. The first man takes a

THE PARTS OF A SENTENCE.

131 step forward, and the second man comes behind him.

The first man steps back and the second man comes forward. Which is nearer to the first man than he was to the third man when the first man stepped forward?

How many times does the first man step forward in one second? What is the distance between the second man and the third man? What is the distance between the third man and the first man? How many times does the second man step forward in one second? What is the distance between the third man and the first man? How many times does the third man step forward in one second ? What is the distance between the third man and the second man? How many times does the first man step backwards in one second? What is the distance between the second man and the third man? What is the distance between the third man and the first man? How many times does the first man go backward in one second? What is the distance between the

How many times does the first man pass backwards in one second? What is the distance between the second man and the first man? What is the distance between the third man and the first man? What is the distance between the third man and the second man?

How many times does the first man go forward in one second? What is the distance between the second man and the first man? What is the distance between the second man and the third man? How many times does the first man go backwards in one second? What is the distance between the second man and the first man? What is the distance between the third man and the first man? How many times does the first man go forwards in one second? What is the distance between the second man and the first man? What is the distance between the third man and the first man? How many times does the first man go back in one second? What is the distance between the second man and the first man? How many times does the first man go forwards in one second? What is the distance between the second man and the first man? How many times does the first man go back in one second? What is the distance between the third man and the first man? What is the distance between the man and the second man? What is the distance between the man and the third man? How many times does the first man come forward in one second? What is the distance between the second man and the first man? distance between the third man and the first man? distance between the man and the second man? What is the distance between the man and the third man? distance between the man and the fourth man?

How many

What is

What is the

What is the distance between the man and the first man?

What is the distance between the man and the second man?

What is the distance between the third man and the first man?

How many times does the first man go backwards in one second? What is the distance between the second man and the first man? What is the distance between the third man and the first man? What is the distance between the man and the fourth man? What is the distance between the man and the second man?

What is the distance between the third man and the second man? What is the distance between the man and the third man? How many times does the first man go backwards in one second? What is the distance between the first man and the second man? What is the distance between the third man and the first man? What is the distance between the man and the fourth man? What is the distance between the man and the fifth man?

What is
```

## R070

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
You stand at the very heart of a sudden, unforeseen catastrophe! The fall is not a gradual or measured matter. it is a swift, relentless descent, and the body in motion beneath you feels nothing to guide it or save it.

We are all of us swept along this same awful power of gravity. I have witnessed many a soul descend from that lofty height. it seems a kind of burial, a sudden arrest of all life and consciousness. The body enters this abyss with a fury that no man can measure or describe. It descends with an almost unabated might, and every muscular contraction and every breath taken in the descent carry weight equal to the weight of our entire frame.

I have seen men fall dead there: their bodies crushed together, their breath gone, their spirits crushed out in that awful moment. The heart that beats in our breast no longer beats there; the lungs no longer breathe; the pulse no longer beats. The soul departs from the body we hold together, and the whole fabric of existence is torn asunder like a piece of paper caught in a storm.

I have witnessed myself fall from such an elevator, and I learned something from that experience that I cannot easily forget: we are not meant to stand upon one spot. This machinery of nature does not pause to our convenience. It operates regardless of our strength, our attention, our will. It is a power that cannot be broken or stayed by our petty calculations of safety or safety.

I have observed that those who fall from such elevations commonly fall upon their feet, or their hands, or both at once. It is not a matter of choice but of necessity. The body has no opportunity to balance itself; it does not stop to think or to act. The heart cannot beat; the lungs cannot breathe; the very breath is swept away in the same descent.

I am told there are men who have spent years in such circumstances, who have been swept down these shafts by this same power, and who have returned to life and strength at a distance from their former body. I have seen such cases myself, and I cannot doubt it. The body in this moment is no longer a companion; it is a burden, a cage, a prison.

This is not a matter of our choice, but of our submission to the universal force of gravitation. It is no problem we resolve by will or deliberation. It is a consequence of this power's dominion.
```

## R071

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
You have touched a most fascinating point in the science of falling bodies, and I am persuaded that you will find it both instructive and rather humbling.

When a stone is released from the hand, we observe that it descends with tremendous force through the air. The stone's weight alone would render it wholly useless at the ground; it would fall harmless to the earth. But when the cable breaks, we find our weight suspended from it. The stone does not come down in a blind blow, but rather performs its descent with tremendous energy and regularity.

I am inclined to think that our friend's gesture of letting go the stone is a revelation of the pull we exert upon the earth. We are not merely pulling against the ground; we are pressing upon it with force equal to the weight of our bodies. The stone is not a passive resistance; it is something we ourselves hold and resist.

I am convinced that this teaches us something very important about the nature of weight: it is not a passive thing to be managed by our strength alone. It is an active force -- one which we exert upon the earth and press upon it with our whole weight. The stone does not fall by chance; it moves under the same pressure that keeps us from falling.

This teaches us that the weight of a body varies considerably according to what it weighs. A man in a carriage or a man standing in an elevator may have no sense of this difference until he lets go his grip or lets fall his stone. The stone is not a inert mass upon which we operate alone; it is a living force pressing upon the earth with momentum that varies greatly according to our size and our strength.

I am inclined to think this also reveals something about the nature of motion itself. A body in motion does not fall by a sudden leap; it moves along its path. We do not strike a stone and withdraw our hand at once; we move our hand along the path we have been moving, and then drop it.

We may say this: our body's weight is not a singular force acting alone upon the stone. It is a coordinated pressure exerted by the whole of our body upon the earth. The stone, in consequence of this pressure, moves along the same path that we have moved. It is not a solitary impulse in motion; it is a simultaneous, sustained force.

We may now perceive clearly why a man in an elevator holds a stone out at arm's length and lets it go. He does not simply throw the stone; he lets it slide along that path which he himself has been moving. The iron pull of his hands is not a single effort driving the stone directly; it is a coordinated pull -- that pull which we exert upon the ground and which is resisted by the same moving force that sustains our own bodies.

This leads us to consider the principle of equilibrium: a body in motion and pressing upon the earth is not a single action alone; it is a composite of many distinct forces acting upon it at every moment of its motion. The stone's fall is not an isolated action; it is the joint result of several pressures -- the weight of our bodies acting upon the ground, the pull we exert upon the earth, the same pull sustained by our own exertions.

I would venture further: we see in this experiment a lesson about the character of motion itself -- it is not a solitary, independent force acting in a straight line; it is a harmonious whole of many forces in concert. It is not a single act of strength alone; it is a complex action -- a force we exert through the combined operation of our muscles, our bodies, and our weight upon the earth.
```

## R072

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
You have touched a most fascinating inquiry, and one I have pondered with considerable attention. I am persuaded that we observe these wandering planets not by accident, but by some influence we cannot yet fully account for, but which we are compelled to admit as a force acting upon them.

I am inclined to attribute this to the very same principle that governs the motions of our own Earth: the attractions of the other planets and comets upon Uranus. In the case of those nearer bodies, their movements may be governed by currents of magnetic or other influences that radiate outward and upward from these distant orbs. The very attraction of Neptune may shape the path of Uranus, much as a magnet shape iron filings.

We have evidence enough that certain planets do not remain in their orbits as fixed bodies. Some wander through ellipses where the influence across multiple bodies varies considerably; others describe curves where the effects are equally distributed. The hypothesis I am framing is that these forces operate unequally upon different parts of Uranus. It is not a fixed body moving in a perfectly stable path; rather, we see a body oscillating between two influences we cannot yet fully account for.

I am further convinced that we ought not to suppose these forces operate in isolation; a system of bodies like ours draws upon the same principle. The planets and their comets alike exert pulls upon one another. Everyone of them draws another, and this pull manifests itself in the planet's wandering in a particular direction. What we call gravitation -- that pull toward every other body -- is felt not in isolated strength, but in complex aggregation.

We are not yet fully accountable for the origin of this influence. It may be one of those threads we discover in the tapestry of planetary motion, a consequence of planetary attraction operating across multiple bodies.
```

## R073

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
You have touched a matter of considerable importance to the study of pendulum motion. I am convinced that the swing of a pendulum is governed by the length of its string or its weight, and not by any mystical property of its form.

Consider the matter thus: a pendulum of one foot in length vibrates just two seconds. A pendulum nine feet in length swings three seconds, a pendulum sixteen feet long swings four seconds. The length determines the swing; the swing determines the time of swing. The string, or its weight, measures the total pull exerted upon the pendulum at every swing. Now, the length of a pendulum is not an arbitrary contrivance; it is the very character of the string's pull that determines the period of swing.

A string of one foot in length vibrates twice in a second; a string of nine feet vibrates four times in a second. The same string, extended or shortened through a quarter of its length, oscillates in proportion. This law holds universally: the length of a string is the measure of the force exerted upon a moving body. The force is not hidden from us; it is measured in terms of a body's weight and its span.

I do not suggest this result is infallible. We are not masters of the string's thickness or the weight of any body we employ. But this principle holds: the length of a pendulum is the measure of the stress exerted upon it at every moment, and that stress is always proportional to the mass it displaces. The same pendulum, drawn out to the extreme limit of its swing, oscillates in the same time as another drawn to a shorter or more pronounced span.

This generalization extends far beyond mere measurement. It tells us that we may choose our unit of mass in varying proportion to our string, and that our length shall be proportional to that mass. The same string that vibrates fastest in a short swing will swing slowest in a long swing; and the time of a swing is proportioned to the mass of the body that moves it.

This principle governs all experiments with pendulums, from the weighing of sand to the timing of a pendulum's motion. It applies equally to all bodies suspended from points or set in motion about centres. The pendulum is not a caprice of matter; it is the expression of the weight of a body and the pull of a string.
```

## R074

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
The weight of the atmosphere, or of what it contains? We have, in the foregoing observations, given some of our reasons for believing that it is the former; but we have also something to say of the latter. We have seen that the atmosphere, when in a state of tension, is the cause of the upward movement of objects, and it is in this upward movement we must look for the real cause of our sense of weight or downward pressure. The atmosphere may be considered as a great reservoir of aqueous vapor, and when it has reached the point of tension it causes the ascent of objects through its upward pressure. As it is in a state of compressibility, its compressibility is increased as it rises, and as it is in a greater volume, its tendency to rise is less. The tension of the atmosphere is the cause of the upward movement of objects, but the volume of the atmosphere is the cause of the ascent of objects. When the atmosphere becomes incapable of compressing objects, and when it has reached a certain point in tension, objects no longer press downward, but upward. Thus, in speaking of the "rising of an object," we

mean the upward movement of the atmosphere, and not the downward movement of the object. When the air is in a state of tension, the atmosphere is the cause of the upward movement of objects, and when it is in a state of compressibility, the atmosphere is the cause of the downward movement of objects; and they are, therefore, in a state of tension and compressibility, and will therefore rise.

The atmospheric stratum which contains the object being, at the time of the fall, in tension, the object is, at that time, in a condition to receive the downward pressure; and when it has reached the point of compressibility, the object, having no force to resist, falls. But, in the process of moving through the air, it is also subject to compressibility and to tension, and, therefore, it is, at this point, in a condition to bear the downward pressure. This is what is meant when we say that the atmosphere is "in a state of tension."

When the atmosphere is in a state of tension, the object is in a state to receive the downward pressure, and the object is thereby made to descend. When the atmosphere becomes perfectly quiescent, the object is in a condition to bear the upward pressure, and the object is thereby made to ascend.

But when the atmosphere is in a state of compressibility, it is in a condition to bear the upward pressure, and the object is thereby made to fall.

When the atmosphere is in a state of compressibility, the object is in a state to become the subject of the downward pressure, and the object is thereby made to fall. When the atmosphere is in a state of tension, the object is in a state to become the subject of the upward pressure, and the object is thereby made to rise. When the atmosphere becomes in a state of compressibility, the object is in a state to become the subject of the downward pressure, and the object is thereby made to fall. When the atmosphere becomes in a state of tension, the object is in a condition to become the subject of the upward pressure, and the object is thereby made to rise.

When the atmosphere becomes in a state of compressibility, and there is no tension, the object is in a state to become the subject of the upward pressure, and the object is thereby made to fall.

When the atmosphere becomes in a state of compressibility, and there is a tension, the object is in a state to become the subject of the upward pressure, and the object is thereby made to rise.

When the atmosphere becomes in a state
```

## R075

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
You have touched a most curious effect of the wind upon a sail, and I am convinced it is the result of a subtle action we have not yet fully examined.

When a wind blows upon a mast, that surface becomes a conduit between the air and the water. The wind presses upon the top of the mast, and the mast offers a certain resistance to this pressure. The stone, we might suppose, does not fall upon the deck at the foot of the mast; rather, it alights at the top, perhaps a few feet behind it, and proceeds straight toward the rigging. Here we observe a curious reversal: the stone does not strike the deck at the foot of the mast, but at the top.

I suspect the explanation lies in this: a stone does not fall directly upon the deck itself; rather, it lands at a slope. The motion of the wind carries it forward, and the mast, being a smooth surface, presents a gradual inclination. The stone, no longer pressed against the side of the hull, arrives upon the rigging with a gentle, upward push.

I have observed this effect often in my own observations, and I find it most arresting. A ship will glide past a quiet bay and a sailor will let a stone fall from the top of the mast. The same action appears again and again, as though the wind itself were a tide advancing along a shoreline. The deck itself becomes a mirror of the wind's direction.
```

## R076

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
You have touched a matter of considerable importance, one I have long pondered and found particularly unsatisfactory.

I am persuaded by the principle that a body cast from a height never truly falls alone. The momentum of the fall carries it forward, and we find ourselves drawn back into our chair or carriage as though we had been released from a pull. This is not a conscious act: it is an involuntary acknowledgment of our weight being drawn forward at each new footfall.

Moreover, we observe that our limbs remain in constant motion during the fall. we are in constant struggle against our nature's propensity to cling to ground. We do not feel the weight of our bodies pressing us back into our seat. We are conscious of our own backward movement, of our effort to push ourselves forward when we are drawn from our position.

I suspect the truth is this: we do not fall alone. we are carried along with our bodies, pressing forward with ever-increasing force during the fall. This forces us to pull ourselves forward into our chair or carriage, and we find ourselves not in a standing position but already in a predicament of urgency. We are pulled backward and our consciousness of our own weight rebels.

I am inclined to conclude that such a person experiences something approaching an escape: he is not pressed back into his seat by his own body, but by something far more powerful. dragged forward in concert with his own motion. That escape is not conscious; it is no effort of will; it is the evidence of our body's complete submission to its own progression.

This suggests we do not feel our weight during the fall, but we are pressed forward by objects that are drawn along with us. The man in a closed carriage feels his weight as a pressure at his back or side; we feel it as a force pressing our body forward. Both are facts of motion, not states of consciousness.
```

## R077

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
You have touched a matter of considerable importance, one I have lately examined with great attention, and I am firmly of the view that the scale you describe represents a most reliable indicator of the moment at which a weight or force descends from a position of equilibrium.

Observe the weighing scale from any position whatsoever. When the cable ruptures, you observe motion to be suddenly accelerated; this tells you at once that the weight has not yet attained its final descent. It arrives with a quick, violent downward thrust, not steady, measured. It moves with a decisive, nearly irresistible force. The scale's indication tells you this.

Now, here lies the crux of the matter: the scale's indication is not always of an equal value. It varies with the weight in motion. A strong man standing on a weighing scale may move his body with a weight of hundreds of pounds, and yet the scale's indication may be one of considerable slackening; a light man, in an equal position, moves only with a gentle, almost imperceptible swing. This tells you, with certainty, that the weight has not yet arrived at its final descent.

I am firmly persuaded that this indicator serves as our most reliable indicator of falling force. A merchant's account of his weight and momentum tells us something quite different from a balance's beam. The scale's movements are not uniform; they vary according to the magnitude of the passing load or the intensity of the momentum of the weight. It is not a uniform standard of force; it is one that responds not uniformly to the same pull, but according to the character of the momentum upon which the force acts.

We ought to measure ourselves, then, in this matter: a man standing on a weighing scale does not bear a uniform burden throughout his fall, but each interval of accelerated descent is accompanied by a separate, decisive moment of motion. The scale's testimony is thus our most reliable indicator of the moment at which a force descends, and the scale's motion is our measure of its force.
```

## R078

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
You have touched a matter of considerable interest to the mind. I am persuaded by your observation that the body cannot bear its weight whilst it remains in motion. A man upon a carriage running down a hill, for instance, experiences nothing of his own gravity during the descent.

But consider another matter: suppose we place a man upon a smooth board in motion and then cast him off without a pull or a push from behind. He does not feel his own weight whilst he falls. His body is pulled forward by the motion of the board, and the weight of his body tends to maintain a straight line at right angles to that direction. The board exerts no pressure upon him; his forward motion acts as a force upon him and bears him away from his seat.

Now compare this with a man who falters from a roof, or who sits upon a fallen tree under considerable pressure. Here we have a different sort of action: the sliding body loses its motion entirely, and the weight of the body acts directly against it. The man does not feel its weight during the fall, because the motion is not in his direction.

I am inclined to conclude that a man in motion bears no weight whilst he moves; the weight of his body acts in a separate and powerful direction independently of his own movements. The carriage falling freely carries forward its own forces; a man falling from a roof carries them with him, and feels the change of his position.
```

## R079

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
You have touched a matter of considerable interest, one I have long suspected without finding a direct conclusion.

I am convinced we must abandon the notion that nature operates with instant force upon the body at the moment of fall. We observe this in the falling of a man, the descent of a stone, the rebound of a ball. The body loses its momentum only gradually: first the legs and arms are bent, then the head bowed, then the whole frame falls together. This gradual loss of force manifests itself in the condition of objects nearby, which are drawn away from the body's motion by their own weight.

I am inclined to conclude that gravity is a gradual agent: its action is not abrupt but continuous. The man's fall does not strike an immediate blow upon his feet or head; it draws away something from the body, and that something lifts a weight upon the floor or the walls of the cabin. This weight may not be immediately felt. It is the quiet and silent pull of the earth, not a sudden assault upon the person's person.

We may now account for more curious effects: a person failing freely from a roof does not feel their own weight during the fall. This suggests that the body's pull is not a sudden, violent push upon the feet or head, but a steady, continuous force. It does not strike at once, but draws away part of the man's momentum gradually. A stone dropped from a height and struck upon a floor does not rebound with a sudden force; it moves steadily, drawing away every part of the stone's body.

This principle appears precisely in nature's operations: we observe it in the motion of falling bodies, in the sinking of a stone upon a plane surface, in the gentle passage of a carriage over a level road. The same force that draws away a body also pulls upon neighbouring objects, whether they are close or distant from the faller's person. It operates more steadily than an instant blow might achieve, and we may conclude with confidence that our experience is a consequence of this slow, uniform pull of the earth, not an instant attack.

We may therefore conclude that a body's fall does not terminate instantaneously, but rather moves through a steady and resistant process: it draws something away from the body, and that drawn weight acts laterally and obliquely, carrying the weight quietly along the floor or wall until it is balanced upon a support or rested upon another object. It is not a sudden blow but a slow, steady action, and this action is the same as our experience of falling bodies -- they are drawn from their height by the gradual pull of the earth, and that pull is always in motion.

This conclusion satisfies my mind better than any theory we presently entertain regarding the instant or suddenness of that descent.
```

## R080

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
You have touched something essential to our present mode of measuring force, and I am pleased you are so concerned with it.

When a man takes hold of the side of an elevator or walks a narrow floor, he does not stand still and allow the weight of his body to settle upon him. Rather, he places his hand at arm's length and lets go. A stone dropped from a height, striking the floor, does not strike upon a man's chest or knees and then pass away. It strikes the floor directly where it is. The force is all at one end; the stone at the other.

Now, observe how this operation varies with the mass of the stone and the height of its descent. If we were to measure the force through the distance a stone falls, we should find it constant. It is not distributed uniformly in the body. It is all concentrated at the instant of impact; the body yields in a single, violent action.

This tells us that gravity acts differently upon different bodies. The same body cannot resist a stress of equal intensity across every direction. It tends to yield in a one‑direction fashion, and here we see the distinction between the motion of a stone and the motion of a man's hand or the action of a load upon a lever.

We thus learn that a force does not distribute itself uniformly among all parts of a body. It acts at a single, concentrated point, and the body yields to that point alone. The man who lets go his stone, therefore, is not standing still at the edge of the elevator floor; he is, in a true sense, standing at the edge of his own character and his strength.
```

## R081

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
You have touched something I have pondered considerably lately, and I find myself in rather strong disagreement with Newton's position regarding the law of gravitation. When we observe Uranus to shift its path in a direction contrary to what we might have expected from gravitation alone, we discover ourselves witnessing something far more remarkable than mere attraction.

We observe an anomalous behaviour, one that suggests we are dealing not with a single force acting from all directions at once, but rather with a distinct agency at work that we have not yet comprehended. I am persuaded we are witnessing something more than gravitation acting in accordance with Newton's generalized law.

We encounter a capricious regularity in Uranus's motion that we cannot ascribe to the action of one body upon another. We perceive a force at work operating in a direction we cannot yet name. We observe it irregularly, at varying angles to our system of bodies, and in a way that suggests a power acting upon the planet rather than pressing it from all directions at once. We cannot explain gravitation as acting uniformly across our heavens; we must suppose an agency at work that exerts its influence at varying angles, and in varying directions, upon the moving body.

I am inclined to conclude this represents something we have as yet not fully grasped: that the gravitational energy we observe operates not in all directions at once, but in more than one direction simultaneously. The law of gravitation explains precisely such irregularities; we cannot account for a planet's restless wandering without attributing to the force a tendency to shift its position. That tendency we are not yet able to assign a precise reason for.
```

## R082

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
You have identified a most instructive phenomenon in nature, and one that speaks to the very heart of gravitation. The falling man's body neither feels his own weight nor is it conscious of it. It is gravity that takes possession of it, and gravity alone controls his descent. If he should attempt to weigh himself, there is no method to do so without using some external instrument, and that instrument would be of no use to him.

Now, as to the cabin itself. Here is the crucial point: the cabin is not a place where a man may be weighed against anything that can be measured with precision. It is a space of space, a form of matter. And if the man is of a given weight, that form of matter shall be compelled to assume that weight. When gravity pulls a body downwards, it must therefore pull it downward as a whole, not merely at a point or part.

This is the whole mystery of gravity. We might reason it out geometrically. If a body were lighter than the fluid in which it floats, it would rise, and the heavier would sink. But gravity is not a force of that magnitude. A man weighing seventy pounds would, in falling from a roof, draw the earth away from his motion. He would not simply stand motionless, for he would be attracted toward the Earth with a force that exceeds his own weight. He would be drawn down by gravity, not merely held in his hand.

The cabin is no stronger than any other object in the room. When the cabin falls, it does not resist gravity as a whole, but rather as a portion of it. That portion is sufficient to make the man fall freely, and the cabin itself is drawn in the same direction. Both are subject to the same law of gravity, and the cabin's movement is subject to the same principles that govern the falling man's motion. It is gravity that makes the roof fall, and it is gravity that holds the man in his descent.
```

## R083

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
A sensation of being in a sort of twilight, of being in a cave of darkness. What happens? A sensation of being in the dark, and of being in a cave of darkness.

What do you call that sensation? It is what we call darkness. What do you call the sensation of

light, and of being in the light? We call it light.

What do you call the sensation of heat and of cold?

We call it heat and cold. What do you call the sensation of water and of ice? We call it water and ice. What do you call the sensation of smell and of taste? We call it smell and taste. What do you call the sensation of sound and of noise? We call it sound and noise. What do you call the sensation of darkness and of light? We call it darkness and light. What do you call the sensation of heat and of cold? We call it heat and cold. What do you call the sensation of moisture and of dryness? We call it moisture and dryness. What do you call the sensation of the sensation of hunger and of thirst? We call it hunger and thirst. What do you call the sensation of a sensation of light and of darkness? We call it light and darkness. What do you call the sensation of the sensation of cold and of heat? We call it cold and heat. What do you call the sensation of the sensation of motion and of rest? We call it motion and rest. What do you call the sensation of a sensation of touch and of pain? We call it touch and pain. What do you call the sensation of a sensation of heat and of cold? We call it heat and cold. What do you call the sensation of sounds and of odors? We call it sounds and odors. What do you call the sensation of a motion and of rest? We call it a motion and rest. What do you call the sensation of the sensation of a sound and of a smell? We call it sound and smell. What do you call the sensation of a sensation of a motion and of rest? We call it a motion and rest. What do you call the sensation of a motion and of rest? We call it a motion and rest. What do you call the sensation of a sensation of light and of darkness? We call it light and darkness. What do you call the sensation of a sensation of motion and of rest? We call it a motion and rest. What do you call the sensation of a motion and of rest? We call it a motion and rest.

1. What is a sensation? 2. What is meant by saying that we have a sensation of a sensation? 3. What is meant by saying that we have a sensation of touch? 4. What is meant by saying that we have a sensation of heat and of cold? 5. Give a list of the sensations of which you have yourself had a sensation. 6. Give a list of the sensations you have had from others. 7. Give a list of the sensations you have had from animals. 8. Give a list of the sensations you have had from inanimate objects. 9. What is the difference between a sensation and a feeling? 10. What is the difference between a sensation and a perception? 11. What is the difference between a sensation and a perception? 12. What is the difference between a sensation and a perception? 13. What are the senses? 14. What is meant by the senses of the body? 15. What are the senses of the mind? 16. What are the senses of the soul? 17. What is the mind? 18. What is the mind? 19. Is there a mind without a body?
```

## R084

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
You have touched a most curious question, one that I have long debated with myself and my friends.

I am inclined to think that the heavier stone descends first, not because it is greater, but rather because the descent is more deliberate. Consider the matter thus: a stone of ten times the weight will strike the ground with a force that is almost instantaneous; a stone of one hundred times heavier strikes it more slowly, and so the difference becomes manifest. A stone of fifty times heavier may come down with a gradual, half-heeded impulse, while the lighter one achieves its fall with full force and strikes the earth with immediate effect.

This suggests that weight is not a fixed condition but a particular quality of motion. A body moving heavily through the air tends to strike with its whole force at once, while a lighter one strikes the same surface with every part of its momentum at once. The stone that moves more slowly than its fellow arrives at the ground with a longer sweep, and its effect is often greater than that of its lighter counterpart.

We are also told that a stone cast downward from a height of some six hundred feet will pass through a distance of three hundred feet before reaching the ground. This suggests that the force of gravity does not change its intensity uniformly; it accumulates at each point of fall through the distance. The heavier stone, by reason of its weight, reaches the ground with a higher velocity than the lighter one, and this velocity is what we observe.

I am inclined to conclude, therefore, that force is not a universal property of matter, but rather a particular pattern impressed upon bodies as they fall through space. The heavier body arrives at the ground with a maximum energy, and that energy is spent largely in producing velocity and altering the momentum of the body before it settles. The lighter body reaches the ground with less force, but with sufficient duration to give its effect.

This explanation accords well with observation and our knowledge of falling bodies. The heavier stone descends with a steady pull, drawing others along with it; the lighter one descends with shorter, more intense effort, and lands with its whole momentum upon the earth. The difference between these two is the fruit of varying velocities and the particular direction of gravity's action.
```

## R085

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
You have touched a matter of considerable importance to the mind. I am persuaded we view gravity as a force pulling bodies downward with an inexorable pull, yet this is a grave error.

A man suspended in a roof by no other support than his weight alone does not find himself weighing at the moment of release. He falls as a lighter body would, and is entirely free of any sense of his own weight until he strikes the ground. The weight is borne by the walls, by the floor, by the table upon which we stand. We do not feel it.

What we observe is not the force of gravity acting upon bodies, but rather the space through which that force passes. When a man falls, the space through which his fall passes is not uniform; it changes with the height of his body and the velocity of his descent. This space is not measured by our scales. It is not the weight of our bodies during the fall. It is the work done by our body in that same moment.

We ought to recognise that gravity acts upon each particle of matter in equal measure. A stone resting upon a firm surface is as heavy as a stone falling freely from a height. The whole body does not alter weight; it distributes that weight precisely as a tree gives its shade to a distant thicket.

I am persuaded this view represents a false account of gravity's action. We measure force by its effect upon a mass or upon other bodies, not by what a fallen body does in its own descent.
```

## R086

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
What is the difference between falling and tumbling? Explain the word "elevator" and its meaning.

In the elevator a large part of our body is in motion, while the remainder is at rest.

What is it that makes a body fall? How is it that the elevator will not fall? Give the general rule for elevators. In what way will the fall of the elevator make your body fall? Explain the action of the elevator. What becomes of the air that is used in the elevator? Can you see the air in the elevator?

Can you see the air that is used in the elevator?

How do you know that the air in the elevator is used? How do you know that air is used in the elevator? What is the rule for elevators? Give the rule for the elevator that falls freely.

What is a "balloon"? Explain the use of the balloon. How does it go? What is the balloon called in any special case? How does the balloon rise? Explain why it does not fall. Can you build a balloon that will rise without being thrown down? What are the advantages of the balloon over a parachute ?

THE SUN.

What is the sun? Explain the sun and the sun-spots. What is a "sun-spot"? What is a solar spot? What is the explanation of the sun's spots? Explain the appearance of the sun-spots. What is a solar spot? What is a solar spot?

What is the sun's distance from the eye?

What is meant by the sun's apparent size? How do you know that the sun is many thousands of miles from you? How do you know that it is many hundreds of thousands of miles from you? Explain the sun's apparent size.

What is meant by the sun's apparent diameter?

What is the size of the sun? What is the sun's apparent diameter? How do you know that the sun is a great distance from you? What is the sun's apparent diameter? How do you know that a great distance from you. the sun is a great

How do you know that the sun is a great distance from you? What is meant by the sun's apparent diameter? Explain the sun's apparent diameter. How do you know that the sun is many thousands of miles from you?

What is meant by the sun's apparent size? Explain the sun's apparent size. What is meant by the sun's apparent size? How do you know that a great distance from you the sun is a great distance from you? Explain the sun's apparent size.

What is the sun's apparent diameter? How do you know that the sun is a great distance from you?

How do you know that the sun is many thousands of miles from you? How do you know that the sun is a great distance from you? How do you know that the sun is a great distance from you?

THE MOON.

What is the moon? What is the moon called by some people? What is the moon in the picture called by some? What is it called by most people?

What is its diameter? What is meant by the moon's diameter? How do you know that the moon is a great distance from you? Explain the moon's diameter. How do you know that it is a great distance from you? What is the moon called by some people? How is it called by most people? What is the moon called by most people?

What is meant by the moon's distance from you?

What is the moon called by most people? Explain the moon's distance from you. What is meant by the moon's distance from you? How do you know that the moon is a great distance from you?

How do you know that it is a
```

## R087

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
You have touched a matter of considerable importance, and I am gratified that you have posed it so directly.

I should answer it thus: the stone from the lower end strikes the ground first. The reason is plain enough: gravity acts upon each stone in succession, and the downward force of one strikes before the other is wholly inert. When a stone falls from a height, the force of gravity does not merely press upon it; it moves it forward. The stone upon the ground reaches its full force only when the force generated by the fall of that preceding stone has already done its work.

This principle applies with equal force to any body. A cannonball from a distance, a stone from a height. each moves with a certain momentum before it strikes the ground. The force acts upon each body in succession, and so does not arrive at the same point simultaneously.

I would go further: a stone shot from a height may strike a second stone at a distance, and pass that distance unresolved. The second stone advances before its impulse is destroyed. The first stone, still in motion, reaches the ground before its full effect is exhausted. This explains why a heavy body falls first, while a light one may glide along a sloping surface or strike a body with little momentum.

We may therefore conclude that gravity acts upon every body in succession, each body completing its full effect before the next arrives at its full force. The momentum generated by a falling stone is always equal to the product of the body's velocity, its mass, and the distance it moves from the point of fall. It is thus equal to the square of the distance it falls through.

This explains why a man standing upon a height, observing a falling stone, feels its force first, and why a ship's anchor that descends from a height strikes with full power. The gravity acts upon each body at precisely the moment it reaches that point, and each strikes with full force.
```

## R088

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
You have touched a matter of considerable importance, one I have long suspected. The experiments I have witnessed with various instruments do not contradict one another, but rather confirm that the two rays operate upon the same medium in an identical manner, yet at differing velocities.

I am inclined to conclude from these observations that the Earth's motion is not uniform or perpendicular to itself, but oblique to it. A body in motion along a line fixed in space does not travel with equal velocity in all directions at once; it moves in a varying curve. The two speeds we observe are parallel to this curve, not coinciding with it.

Moreover, I am inclined to infer that the rays are not transmitted along a straight line but along a flexible one. The medium through which they move is not a perfect plane; it is a spheroid. The two rays strike different portions of this surface at varying angles, and the two speeds may differ from one direction to another.

We might therefore conclude that the medium of space itself is not a uniform plane but a spheroid, and that the two rays are not transmitted along a straight line but along a flexible one. This suggests that the two speeds are related to the body's motion, in a manner we experience when we observe them at differing angles.

I am further inclined to suspect that we observe this phenomenon because the body or medium possesses a different elasticity at different directions. The two rays possess different properties in virtue of this different elasticity; they are not travelling along a single straight line, but following different curves.

I would venture this: the two rays do not emanate from the same point in a straight line, but from different points along the same body or medium, and the two speeds are determined by the body's motion at different angles. The light thus does not travel along a single straight line, but a curve of its own.
```

## R089

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
What part of the ship is it? How is it to be found? How much of the ship is represented by the figure?

What is the part of the ship which is represented by the figure? How much of the ship is represented by the part of the figure represented by the line?

What do we call the part of the ship which is represented by the line?

How is it marked?

How many parts of the ship are represented by the line?

How many parts of the ship are represented by the part of the figure represented by the line?

Where is the part of the ship represented by the line?

Where is the part of the ship represented by the part of the figure represented by the line?

Where is the part of the ship represented by the part of the figure represented by the line?

Where is the part of the ship represented by the part of the figure represented by the line?

How many parts of the ship are represented by the line?

The part of the ship represented by the line is represented in the figure by the line.

Ships are represented in a ship by lines.

In what way?

How many lines are represented in the figure?

What are they called?

How many lines are represented by the part of the figure represented by the line?

Point out the parts of the ship represented by the line.

What are they called?

How many lines are represented in the figure?

What are they called?

What part of the ship is represented by the part of the figure represented by the line?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

What part of the ship is represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure represented by the line?

How many lines are represented in the figure?

What are they called?

How many parts of the ship are represented by the part of the figure
```

## R090

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
You have touched one of the most fascinating aspects of the motion of bodies when they meet one another upon the surface of the earth. In such circumstances two stones arrive at precisely the same moment upon the same stone.

I am inclined to think this arises from the same law of gravitation which governs all other bodies we observe upon the earth's surface. When a stone reaches the ground, it does not leap entirely free; it strikes the ground with a certain force. But this force is not instantaneous; it is gathered over a considerable interval of time. The stone descends with a certain velocity acquired in its descent, and before that velocity can be exhausted, it meets the ground.

Now, consider the other stone which we have described: it falls at a different angle, with a lesser velocity. It strikes the ground with a smaller force, and therefore does not acquire that velocity in a moment. Rather, it strikes the ground only after a considerable interval of time. The velocity spent in striking the ground is not instantaneously exhausted; instead it is accumulated and stored up in the stone, much as a reservoir of water is stored in pipes.

The two stones strike each other with identical effect: at precisely the same moment, and each receives the same shock upon reaching the ground. This principle governs every motion we observe in the natural world. It explains why a stone thrown from a height descends with precisely the same force it would expend in falling from a height equal to its own distance from the earth's centre.
```

## R091

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
What is the effect on the sailor as he takes his place in the rigging?

What is the result on the ship, the sailor, and the rigging?

Animals walk. A horse can walk, a cat can walk, a tortoise can walk. What is the difference between the progress of these animals and that of a man? Which moves more quickly, a tortoise or a man? A horse, a dog, or a man can run. Are they all alike in this respect?

Which can run faster, a man or a tortoise?

A man can walk, a horse can trot, a dog can run.

Which has the more power of endurance, a man or a horse? Which is the more agile? Can you tell why?

Which has the more intelligence? Can you tell why?

Which is the more cheerful? Can you tell why?

A cat can jump. Can you tell why?

A man can lift a heavy weight. Can you tell why?

A horse can trot. Can you tell why?

A dog can run. Can you tell why?

A dog can bark. Can you tell why?

A dog can howl. Can you tell why?

A man can see. Can you tell why?

A man can hear. Can you tell why?

A little boy can sit up straight. Can you tell why?

A little boy can walk. Can you tell why?

A little girl can dance. Can you tell why?

A little boy can play ball. Can you tell why?

A little girl can play croquet. Can you tell why?

A little girl can play checkers. Can you tell why?

A little girl can play marbles. Can you tell why?

A little girl can play foot-ball. Can you tell why?

A little girl can play base-ball. Can you tell why?

A little girl can jump. Can you tell why?

A little girl can jump over the fence. Can you tell why?

A little girl can jump over a chair. Can you tell why?

A little girl can jump over the fence. Can you tell why?

A little girl can jump up on the platform. Can you tell why?

A little girl can jump up on the door-step. Can you tell why?

A little girl can jump up on to the roof. Can you tell why?

A little girl can jump down on the floor. Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump down from the top of the house.

Can you tell why?

A little girl can jump up from the top of the house.

Can you tell why?

A little girl can run. Can you tell why?

A little girl can run. Can you tell why?

A little girl can run across the street. Can you tell why?

A little girl can jump up from the floor to the ceiling.

Can you tell why?

A little girl can jump up from the floor to the ceiling.

Can you tell why?

A little girl can jump up from the floor to the ceiling.

Can you tell why?

A little girl can jump from the floor to the ceiling.

Can you tell why?

A little girl can jump from the floor to the ceiling.

Can you tell why?

A little girl can jump to the top of the house. Can
```

## R092

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
What is the effect on the cable? Would it be possible for a man to stand in the elevator without danger? Would a man in the elevator stand in a position of safety? What is the cause of danger? What is the principle which you learned in the last lesson? What is the principle here taught? What is the principle of the pulley? What is the principle of the wheel and axle? What is the principle of the inclined plane? Can you give any illustrations of the principle of the pulley? Show how the principle of gravity acts in the air. Explain the air-pump. What is the principle of the air-pump? What is the principle of the barometer? What is the principle of the air-gun? What is the principle of the windmill? What is the principle of the water-wheel? What is the principle of the air-pump? What is the principle of the pump? Can you give any illustrations of the principle of gravity? What is the principle of the windmill? What is the principle of the water-wheel? What is the principle of the air-gun? What is the principle of the water-wheel? What is the principle of the windmill? What is the principle of the water-wheel? What is the principle of the air-gun? What is the principle of the windmill? What is the principle of the water-wheel?

D. APPLETON & CO., PUBLISHERS.

THE PRINCIPLES OF THE MECHANIC ARTS.

By Professor H. W. BAIRD, of the University of Glasgow, author of "The Application of

Mechanical Science to the Useful Arts," "The Mathematical Theory of the Steam-Engine," etc.

16mo. Cloth, 110 pages. Mailing Price, 65 cents. Introduction, 50 cents.

THE

HE author has endeavored to present the subject in such a way that the student of mechanics may not only readily comprehend the reason of the rule, but may be able to apply it to practice.

The book is arranged in the most simple manner, and is designed to lead the student to the knowledge of the subject itself. The propositions are numbered, and the student is required to refer to the corresponding section in the text of the work. The tables of mechanics are given with the explanations, and these, by reason of their simplicity, are easily mastered.

The book is intended for the use of students who have made considerable progress in the study of mechanics, and who are beginning to attempt the study of general mechanics.

The work has been prepared for the purpose of simplifying the study of the subject, and of making it as clear and simple as possible.

In the treatment of the subjects of the chapters, the author has endeavored to combine simplicity with fullness of explanation. The different propositions are separated from each other by brief statements of the reasons for the rule.

HORNER'S SERIES OF SCHOOL GEOGRAPHIES.

I. THE PRIMARY SCHOOL GEOGRAPHY. 16mo. Cloth. 114

pages. Mailing Price, 50 cents; Introduction, 40 cents;

Questions, 20 cents.

II. THE INTERMEDIATE SCHOOL GEOGRAPHY. 16mo. Cloth.

96 pages. Mailing Price, 50 cents; Introduction, 40 cents; Questions, 20 cents. 10

D. APPLETON & CO., PUBLISHERS.

THE PRINCIPLES OF THE MECHANIC ARTS.

By Professor H. W. BAIRD, of the University of Glasgow, author of "The Application of Mechanical Science to the Useful Arts," "The Mathematical Theory of the Steam-Engine," etc.

16mo. Cloth, 110 pages. Mailing Price, 65 cents
```

## R093

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
You have touched something very peculiar to our present mode of conveyance. When the cable breaks and the elevator descends, we witness a reversal of what our daily motions and observations suggest.

We observe that a carriage or a weight upon a slope is not left at rest; it is set in motion away from the earth's centre. The downward motion is not uniform; it is governed by gravity. When a load descends, the weight tends to fall in a direction opposite the direction of gravity: it presses upon the floor, turns the carriage, and forces the bottom of the elevator to move downward. This tendency is not uniform; it varies according to the weight and the distance of the load from the point of support.

Now, why should gravity act in this manner? We answer it thus: the earth acts upon every body it bears, bending it toward its centre. When a weight falls upon a smooth surface, the downward pull upon the floor is not uniform; it is strongest at the point where the weight rests directly above the centre, or at the centre of the slope itself. The motion of the carriage, then, is not uniform: it is set in motion toward the centre of gravity, a direction opposite to what we might suppose a body to receive at rest.

This reversal of motion is no accident. It suggests gravity is not a force exerted at random, but a system of forces that act in concert at every point from the centre of gravity to every edge of a body. The elevator does not fall freely in a straight line; it is forced to glide down an inclined slope, and gravity presses upon every side of the motion at once. It is a powerful force, but it is not uniform. It acts at every angle of direction, and we witness the effect of this action in our every motion.

We observe this as we descend a steep hill or ascend a winding stair. The descent is not uniform; it is governed by gravity and the geometry of the slope.
```

## R094

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
Your observation is most apt, and I would commend the gravity with which you have approached a problem which has exercised the minds of the greatest astronomers since the days of Kepler. The phenomenon you describe is not an anomaly but a reflection of the great principle that no material object can, in its own direction, remain stationary in space.

The key to the matter lies in the nature of the force that governs the orbital motion of bodies. In the case of the planet Uranus, the gravitational pull of the fixed stars upon its surface is such that its path must depart from the path of the Earth. This departure is not a mere accident of its own orbital motion; it is the effect of an external influence that can be discovered by proper mathematical method.

In the first instance, consider the nature of the Earth itself. The Earth and planet Uranus are bound in a common sphere, and their orbital motions are therefore compounded by the mutual attraction between their surfaces. This reciprocal attraction produces a force that acts upon the planet with a regularity that is, as far as we know, independent of the planet's orbit and its own mass. The Earth possesses a stable relative position with regard to the planet; the planet thus experiences no periodic oscillation in its orbital path.

Now, the orbital motion of Uranus alone would be sufficient to account for a small amount of apparent deviation. But when we consider the planet's influence upon the earth's atmosphere and the planet's rotation upon its axis, we find that the deviation is indeed considerable.

The explanation lies in a principle of gravitational action we call gravitation. The Earth's attraction upon the planet Uranus is directed toward its centre, and the forces are thus directed toward the centre of the planet's orbit. Moreover, the Earth's attraction upon the Moon and the planets causes a slight curvature of the planet's path.an effect that may be observed in the behaviour of the planets with their inner satellites.

When we consider the planetary distance from the sun, the variation of gravitational effect is still greater. The planet's orbital velocity is not the same at all seasons; it is smaller when it passes near perihelion, larger when it passes near aphelion. The observed variations in the planetary distances correspond to the precise effects of these forces.

The planet Uranus, then, is not fixed in space, but is subject to a net effect of orbital and gravitational forces upon its path. This is not an anomaly but a consequence of the mutual attraction between them, and a consequence that Newton himself, ever the mathematician, has demonstrated to be predictable by the principles of physics.
```

## R095

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
You have touched a matter I have long observed with curiosity, and I am inclined to think the scale tells us a great deal about the man's character and the nature of his situation.

When a man descends from a height by a rope, or by the weight of a vessel or its own descent, we witness that peculiar tension between muscular strength and the element of uncertainty. We observe the muscles contract and the shoulders raise, the spine bend, and the whole frame strain. We see this not merely in the body's motion, but in the look of the eyes and the tension of the mouth. When a man stands upright, we see a certain composure; when he descends, we witness a kind of uneasy or tremulous motion we find almost incompatible with perfect strength.

Now, observe what the scale shows: after the weight falls, the muscles relax, the shoulders droop, and the eyes lose their confidence entirely. This is no accident; it is the expression of a man's nervous system and the very nature of his condition. We might say he is being rescued from uncertainty, or that he feels a loss of his own strength.

I am inclined to infer also from this that the scale tells us something about character. We observe men of different temperaments, as you have noted, ranging from one who walks with confidence to another who stands motionless. We see them differentiated by their circumstances. The same man standing upright might appear resolute and resourceful, but when he descends and sees the elevator fail, we witness a different man entirely. He is not a man of extraordinary strength, but one whose will is tempered by the knowledge of his position.

This lesson ought to be a warning to those who would venture into positions where a rope may snap or a vessel may strain. The scale tells us something we cannot help observing: that an uncertain situation produces different effects upon the character than an absolute certainty.
```

## R096

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
What is the meaning of the phrase "laid the stone," or "lying the stone"? Ans. It is a part of the captain's duty to see to it that the stone is laid at the proper place, and then, when the ship is at rest, the men fall to and lay it there. See notes at the end of the lesson.

What does the phrase "lay the stone" mean? Ans. It means to lay the stone to the proper place. What was the stone to be laid for? Ans. It was to be a mark or landmark, to show where the ship was, and how far she had sailed.

What is a mark or landmark?

Ans. It is a sign by which we know where we are, or are to sail.

LESSON 6.

Ex. 14: 2. And when they had found the young child, they asked him of his father, and of his mother, and no man could give them any answer.

What does the phrase “found the young child” mean? Ans. They found him in the arms of his parents.

What did they ask him? Ans. They asked him if they might carry him home. What is a home? Ans. Any place to which one is brought up, and where he is at home.

What is the difference between “home” and “place of one's nativity"? Ans. There is a difference between the two phrases, the one is a place which one has chosen for himself, the other is a place into which one has been brought up.

Is this the first time we have heard of Jesus Christ? Ans. No; we read of him in the Old Testament.

What is the difference between the Old and the New Testaments? Ans. The Old Testa ment was a written revelation of God, and the New Testament was a written revelation of God to man. "The Old Testament" is

Name the books of the Old Testament in order. the name given to the Hebrew Bible.

The New Testament is the book of the New Testament or New Testament, and is the book of God's revelation of himself to man.

What is the New Testament? Ans. The book of God's revelation of himself to man.

What is the meaning of the phrase "the book of the New

Testament"? Ans. It means the book of the New Testament, or New Testament.

What is the difference between the Old Testament and the New Testament? Ans. The Old Testament was a written revelation of God, and the New Testament was a written revelation of God to man.

What is the difference between "the Old Testament" and "the New Testament"? Ans. The Old Testament was a written revelation of God, and the New Testament was a written revelation of God to man.

What is the meaning of the phrase "the book of the New Testament"? Ans. It means the book of God's revelation of himself to man.

LESSON 7.

Ex. 2: 10. And when he came to his father, he said unto him, Father, I have sinned against heaven, and before thee, And am no more worthy to be called thy son: make me as one of thy hired servants.

In the preceding lessons the children have been taught to read, write, and speak the English language. They are now to learn the meaning of what is called the English Bible.

What is the meaning of the phrase "the English Bible"? Ans. It means the English Bible or book of the English Bible.

What is a book called? Ans. A book.

What is a book called in the Old Testament? Ans. It is a book, or the book.

What is the meaning of the phrase "English Bible"? Ans.
```

## R097

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
You have touched a matter of considerable importance in the measurement of motion, and I am persuaded that such observations reflect a principle as universal as the Pendulum itself.

Consider the pendulum first: it hangs by a thread from a point of support, and as the weight of the material and the pull of gravity cause the thread to contract or elongate, so too does the length of the pendulum alter its swing. A pendulum of one foot in length will swing but once in a second; two feet will swing twice in a second; three feet will swing three times in a second, and so forth. Now, observe: a pendulum of nine feet in length swings four times in a second, and nine times in a second. The length of a pendulum depends upon this principle: it measures the force with which the weight or the pull of gravity draws the material nearer to the line of motion.

The same rule applies to bodies of variable shape. A rod of iron one hundred and fifty feet long will swing in about two seconds; a rod of half that length will swing in about one second. The length of a body determines, in a manner we shall presently see, the velocity with which that body moves. The shorter body moves faster than the longer one, and the speed increases as the square of the distance traversed.

I am persuaded we ought not limit our observations to a single unit. A pendulum of ten feet long, reaching to the same point of suspension, will swing in about three seconds; a pendulum of nine feet reaching to a different point will swing in three seconds. This is not a matter of accidental variation; it is a law governing the motion of all bodies that fall or are drawn in a straight line. We might say that the length of a body determines its velocity, and the velocity determines the distance through which that body moves in a given time.

This principle extends wide: it applies equally to all bodies and all directions of motion. It is not a mere arbitrary fancy of men of science; it rests upon the evidence of our senses and the universal operation of force upon matter.
```

## R098

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
You have touched a matter of considerable interest, one I have long pondered with some attention. I am inclined to believe that the heavier stone descends under a pre‑established law: the heavier body descends with a force that exceeds the lighter body in a ratio equal to the difference of their specific gravities. This is not a mere coincidence; it is a matter of necessity: the heavier body offers a greater resistance to the air; a force may be enough to overcome that resistance and cause the body to fall. The lighter stone, by contrast, offers less resistance, therefore must be moved less swiftly or else strike with a diminished momentum.

I have also reflected on the principle of motion in bodies falling at right angles to one another. If two bodies strike from opposite directions, one will strike with double the momentum of the other. The greater weight of one of the stones yields this advantage: it strikes with a momentum sufficient to overcome the lesser resistance presented by the lighter body and to carry it forward. Thus the two stones reach the ground together, each one having accomplished its purpose.

I am inclined to conclude that all bodies, great and small, fall upon the same principle: the heavier body descends with a force equal to the difference between its weight and the lighter body's weight, and this force is what we call momentum or striking power. The lighter stone, being lighter in a small proportion, moves with a less momentum, and therefore strikes later than the heavier one. Both fall together, and when they strike, they are one whole at the ground.
```

## R099

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
The answer is that if any such difference exists it would be such that the rotation of the Earth would occur at the same time.

And at all other points of the orbit, if the rotation of the Earth is not in one direction, that is, in the same direction as the Earth's motion, the time of rotation is not at the same time, but it is in the opposite direction, that is, in the same direction as the Earth's motion.

Therefore, if the rotation of the Earth is not in one direction, it is not at the same time, but it is at the opposite time, to the rotation of the Sun.

The whole action of the Earth, then, is in the line of its motion, and the line of its motion is the line along which its rotation is performed.

The difference, then, between the two motions is not in the Earth, but in the Sun.

If the Sun is not at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the two motions are in the same direction. If the Sun is not at rest, but the Earth is, then the Sun's motion is in the direction of the Earth's motion, and the Earth's

THE EARTH.

Motion of the Sun and Earth.

Difference in Time.

Motion in the Direction of the Earth's

Motion.

Motion in the Direction of the Sun's Motion.

Time.

Rotation of the Earth.

Time.

Rotation of the Sun.

Motor.

Time of Rotation.

Summer.

winter motion is in the direction of the Sun's motion.

If the Sun is not at rest, but the Earth is, then the Sun's motion is the Earth's motion, and the Sun's motion is the Earth's motion, and the two motions are in the same direction.

The difference, then, between the two motions is not in the Sun, but in the Earth; and the Sun's motion is the Earth's motion, and the Earth's motion is the Sun's motion.

If the Sun is at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the two motions are in the same direction.

If the Sun is not at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion.

The difference, then, between the two motions is not in the Sun, but in the Earth.

If the Sun is at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the two motions are in the same direction.

If the Sun is at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the two motions are in the same direction.

If the Sun is at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the two motions are in the same direction.

If the Sun is at rest, then the Earth is at rest, and the Earth's motion is the Sun's motion, and the Earth's motion is the Sun's motion, and the two motions are in the same direction.

The difference, then, between the two motions is not in the Sun, but in the Earth.

The Sun's motion is the Earth's motion, and the Earth's motion is the Sun's motion, and the two motions are in
```

## R100

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
You have touched a matter of considerable importance, one I have long suspected might prove otherwise than we commonly suppose; I find it more consistent with reason to conclude that a falling body does not feel its own weight whilst resting upon the roof. The fall from a height does not produce a sudden consciousness of heaviness; rather, it forces every thing within that body to behave according to the laws of gravitation we have already observed.

Consider the matter thus: when we stand upon the ground, we are not conscious of our own muscular effort. We do not feel the weight of our bodies whilst we press upon a stone or walk down a steep hill. This is not because we cannot perceive our own pull upon our legs or our tendency to sink. It is because the weight of our bodies is balanced against the weight of the earth and the resistance of the air around us. The body does not act as a solitary force; it is a living whole, composed of its parts and the forces that keep them in equilibrium.

A man falling from a roof does not feel his own weight. He does not feel the weight of his body as he rests upon the edge of the building; he feels only the weight of the ground and the resistance of the air at those moments where his vertical motion begins. This tells us we are not conscious of our own power; we are not conscious of our own downward pull. It is the law of universal gravitation acting upon every point of a body simultaneously.

I am inclined to conclude, therefore, that a falling body does not feel its own weight until it has already been lifted from the place where it rested. It then becomes aware of its own power, and this knowledge operates upon the mind through its own proper faculties of perception. The falling man knows not his own strength; he knows only the pull of the earth and the resistance of the air around him.
```

## R101

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
You have touched upon a principle that has occupied philosophers for centuries, and which yet remains to be fully understood. The law of propagation, as Newton himself called it, is this: the velocity of light in any medium is proportional to the square root of the absolute index of refraction.the ratio of the wave length to the index of refraction. For instance, in air, the wave length is approximately 1/1 millionth of a centimetre, and the index of refraction is roughly 1/1 millionth. Thus the wave length in air is 2/3 of the wave length in water or in glass. And so the velocity in water is roughly 1/5 that of light in air, and in glass it is roughly 1/4.

Now, if we imagine two rays of light, each of a different wave length, coming from different sources. say, a lantern and a lighthouse. and that two observers stationed at those two positions are simultaneously observing the same light. then the transmission may be compared in different ways. The apparatus I have described consists of a graduated mirror, and a source of light upon the table, from which two distinct illumination systems are cast upon the mirror. The two systems travel from the source along the same path. The mirror receives them at right angles, and they meet at a point, and therein the mirror reflects the light back in the opposite direction. Here the two systems travel in precisely opposite directions, and the mirror returns them in parallel lines to the observer.

The equality of illumination is thus a direct consequence of the wave length. and it remains so until we can construct a physical medium that transmits the wave length and not the wave itself, or until we have a means to measure the wave length directly. But for the present we must content ourselves with the laws of transmission and reflection, as Newton has furnished us.

The most elegant measure of velocity is the time of transmission measured in seconds. If light traverses a second of space before arriving at the eye, and the mirror returns a velocity of roughly 192,700 miles per second, the transmission occurs at a speed of roughly 192,700 miles per second. a velocity that rivals that of a bullet, and which is the same whatever the nature of the medium through which it travels. Thus the wave length that reaches the eye of a man is virtually instantaneous.

The velocity of light in gases, liquids, or solids is similarly expressed by the same law of wave lengths. the velocity is the square root of the absolute index of refraction, as Newton himself observed, and the velocity in a gas is the square root of the velocity in air, and in an ether it is the square root of the velocity in light. It is a consequence of the law of the propagation of motion through a medium.

Thus, light is transmitted not by particles of matter, but by the displacement of the medium, and the velocity with which it travels depends upon the absolute index of refraction and the wave length of the medium traversed. The velocity is directly as the square root of the absolute index, and inversely as the wave length directly. This law, which we have now grasped, governs the transmission of light throughout nature and into our eyes, where it is reflected and refracted to reach us.

The distance from the source to the mirror is not infinite. The rays of light are a series of waves, and the medium through which they travel is a series of molecules. So the distance is not absolute but relative, and the transmission proceeds with a velocity proportionate to the square root of the absolute index of refraction. This law, discovered by the diligent investigations of philosophers, remains the foundation of our understanding of light, and it stands in intimate connection with the
```

## R102

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
You have touched upon one of the most fascinating paradoxes in the whole of Natural Philosophy. The gravity that sustains our bodies is not a force of itself; it is the very thing we call ourselves. The muscles that lift the body and the lungs that breathe are merely the instruments by which this principle works, and the body itself is governed by a law that we term the law of gravitation.

When a man falls, the muscles of his limbs are not a force in themselves; they are the agents of the will. And yet, that will, though it seems to us an almost mechanical thing, is in truth a matter of the greatest delicacy. A man who falls from a height of several hundred feet has not merely his weight to consider; he has the whole of his body's weight, his weight as a whole, and the weight of his very breath together. This together with the weight of his body constitutes his total downward load.

Now, if a man falls freely, the weight of his body becomes almost nothing at the moment of contact. It is as though his body itself were but a feather, and the earth beneath him were the solid ground. His weight is the sum of the weight of his body, the weight of his breath, and the weight of his own weight.

He falls with a speed so remarkable that we can scarcely measure it. He reaches the ground with a force that would knock a stone in pieces. Yet he has not felt his own weight. He has merely struck the earth. His weight has not yet reached him. But then, after this fall, he is perfectly aware of the magnitude of his fall. He has felt his weight, and he has felt the force of his own body.

The mystery turns upon this: not all bodies fall with equal speed; a man falling freely travels through perhaps thirty feet in a second, while a body falling from a height of several hundred feet travels through thirty feet in the same interval. The force of gravity that drives us down is as much a product of the earth's attraction as it is of our own weight. When this force acts upon us, it is not the force of the falling body itself, but the combined effect of the weight of our bodies, the weight of our breath, and the weight of our own body together. It is a force that we cannot measure in pounds and feet, but we can perfectly understand its magnitude.

Now, what of the man who falls from a height of several hundred feet? His weight is considerable, as a man would be expected to weigh forty pounds. But even by the same rule that applies to a few feet, he falls as far as he would fall from a height of five hundred feet. He has not merely fallen; he has fallen to a greater distance than his own height. Every foot he stumbles, every inch he lifts, every inch of distance he opens.all of this is the work of gravitation upon him.

The gravity that sustains us is not a mere force of the earth's attraction; it is a force that pulls all bodies toward the earth, and it is so perfectly uniform that we rarely perceive it. But it is none the less real. A man who falls from a height of several hundred feet has fallen upon the earth's surface, and the surface of the earth is not a mere flat plane, but a sphere of enormous dimensions. The weight of his body is simply one of the consequences of gravity. When he falls, he is drawn downward by gravity, and the earth is drawn downward by him. Both forces are working in concert to produce the fall.

There is also the question of whether the earth itself moves through space with uniform motion, or whether it is subject to some small variation in its velocity. But the principles that guide gravitation and the motion of bodies alike
```

## R103

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
The scale indicates the force exerted upon the cable, and the magnitude of the descent. If the cable were drawn upward vertically, it would indeed exert a downward force upon the elevator, and the cable would not release the elevator freely. This force would be measured by the weight of the elevator and cable itself, and by the weight of the person and the load attached to the elevator. The falling of the elevator therefore indicates not only the force applied, but the manner of its application.

When the cable breaks, the elevator and cage descend with a suddenness that speaks to the nature of the break. The cable, being a yielding, brittle thread, will snap under the weight of the cage and the weight of the descending load, without the cage itself exerting a great force. The cage does not strike the floor, but rather settles into the trap of the fall. If the cage were still held, the force exerted would be a continuous one, and the cage would persist in its descent, moving gradually along the line of descent.

This principle of the falling cage teaches us that the gravity of the load, the velocity of the descent, and the resistance of the cable are interdependent. The cable's speed, when it breaks, is precisely the same as the speed of descending bodies. The cable does not leap downward in a sudden, violent fashion, but rather drags the cage along with it. The rope that holds the cage is not a fixed obstacle but a yielding one, and the brake upon the cage is merely a momentum force brought to bear through the chain.

The downward force upon the chain is not uniform; it varies with the weight of the cage, the velocity of the descent, and the length of the cable. When the chain is short, the cage is drawn up with greater speed, but when the chain exceeds a certain length, the weight of the cage and the cage's own mass can counterbalance the downward force, and the cage settles with greater deliberation. This principle extends to any system of connected parts, whether the cable be in a straight line or a series of pulleys, and it applies to all engines, whether they be machines or animal propulsion.

The scale of the weight of the cage and its load tells us something further: the magnitude of the brake required to arrest the cage in motion is proportional to the amount of load at the brake. A heavy cage requires a comparatively strong brake, while a lighter cage requires a lighter brake. The scale of the brake measures the force necessary to arrest the cage, and the scale of the cage measures the load it bears. It is a useful art to calculate the brake required for a given load, and to remember that this number is proportional to the length of the cable and to the velocity of the descent.

One may also employ the scale to measure the energy of the brake, for the weight is itself the measure of the brake's power. So the scale tells us the magnitude of the brake, the weight of the cage, and the velocity of the descent together make up the force that brake the cage. This is a mathematical truth, and it is worth understanding carefully.

In practical terms, the scale is often written in inches or in hundredweights, and a competent mechanic will compute the brake required to arrest a cage of a given length, load, and velocity, and will compare it with a known measurement of the cage's own load. The comparison may be made in various ways: by weighing the cage itself, by measuring the load of the cage, or by comparing the brake required to arrest a cage of given length and weight against a known brake required to arrest a similarly large cage.

In short, the scale of the cage is a physical record of the force exerted upon it at every moment, and the scale of
```

## R104

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
You have touched a most delicate and instructive contrast I have observed in my experience of such mechanical elevators. The elevator falls with a terrible force, leaving one trembling in every limb. Yet I have learned from observation that the shock is not solely the weight alone which strikes us, but something far more terrible: the sudden reversal of our position.

When we stand upright we are at our most comfortable equilibrium. We are in our proper position for ease and composure. But suddenly we are transformed from that position, our feet striking the floor with frightful force, our hands grasping the iron railings or some solid support beneath us. I have noted that the body's action does not merely change its centre of gravity; it throws our whole frame into a kind of violent vibration.

It is not merely the weight that strikes us. It is the entire alteration of our placement. The brain, the muscles, the very bones of our limbs all bear witness to this shock. I remember once seeing my dear nephew descend a flight of stairs at a railway station and his face turned white as the marble floor above him. When I set him upon his feet, he fell back in my arms and spoke almost in a whisper of that moment of terror.

I have observed that these accidents occur with little damage to life or limb, and that the descent is accomplished with a swiftness that seems almost providential. The law of motion itself teaches us that a body does not fall by mere weight alone; it must be altered in equilibrium. The descent transforms our position entirely.
```

## R105

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
You have identified a most fascinating misconception, and one which has occupied the minds of natural philosophers for centuries. The question is this: gravity is not a force acting upon bodies in motion, but rather a force which binds the earth to bodies at rest.

Consider a pendulum swinging, and you will acknowledge this immediately. It is not the length of its swing, but the direction of its swing, which determines the duration of its motion. If a pendulum were to swing freely, the swing would be uniform and would occupy the same time. If it were to fall from a great height, the fall would be accelerated, and the descent would be accelerated equally, as the law of falling bodies asserts. The acceleration would not depend upon the mass of the body itself but upon its velocity of motion.

Now when a man drops freely from a roof, the fall itself is accelerated. The roof does not pull the man down with uniform force. The roof's pull is concentrated upon the bodies that rest upon it. The roof is not a body dragged from its position. It is a body held in place by the weight of others below it. The man's weight draws him down with a speed that increases with his distance from the earth.

The analogy with a pendulum is instructive here. The ball, by reason of its weight, descends with velocity increasing as the square of its distance from the point of suspension. A body moving freely, however large it may be, tends to fall with a uniform velocity. This law holds whether the body be of iron or of the most minute feather. It is not a contradiction that the great weight of a mountain should produce a motion of great velocity, yet the velocity is determined by the distance traversed and the magnitude of the mass.

The error lies in supposing that gravity acts as a single force upon bodies in motion. This is not the case. Gravity is a complex force, composed of several independent components. The velocity, the direction, and the distance all vary according to the nature of the body upon which the force acts. The weight of the body exercises no pull upon it, for it does not press upon it. But the weight of the earth exerts pressure upon every particle. This pressure is transmitted downward, and downward through the air and the ground. This downward force accounts for the motion of a falling body.

When a man drops from such a height, he does not move downward with a uniform velocity. He moves with a composite velocity. The velocity is proportional to the height from which he fell, and the distance traversed is proportional to the square of his height. The body's motion is determined by the two components of gravity.gravity accelerates the fall, and the velocity produced is proportional to the height from which the body fell.

The body falls freely, as a pendulum falls, because it is already under the influence of gravity. The force of gravity acts upon it at every moment, and if the body cannot resist it, it will fall. But if it is already falling, the force of gravity is already acting upon it.only in the case of a free falling body does it exert no influence upon the body's motion.

So far, so noble. But here is where confusion enters: if the falling body is already under the influence of gravity, the effect of gravity is not simply to accelerate it, but to accelerate it more rapidly than if gravity acted alone. Gravity does not simply help a body fall. It helps it fall faster than by itself.

And yet the law of falling bodies is equally true for the earth itself. The earth's gravitation draws bodies toward its surface and accelerates their fall. But the atmosphere and the bodies upon the earth are already under the influence of gravity, and gravity acts upon
```

## R106

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
You have touched a matter I have often debated with myself, and I find it rather persuasive to our notion that weight is not a fixed thing but a variable one.

A stone dropped from a height descends with a certain swiftness and force upon the floor. I find I can count the separate beats of my counting-house clock, I can measure the passage of my carriage wheels over the cobblestones, I can observe the weight of a grain of sand as it falls through the air. Each of these observations tells me that weight is subject to variation. We do not merely hold our stone out of hand and let it fall. we notice the motion of the stone, the angle it makes, the force with which it falls. We learn that a stone may change its rate of descent and therefore its power of destruction.

Now, when a man holds his stone in his hand and lets it fall, what happens? The stone does not simply strike the floor with full force. It is broken into several fragments, each carrying its own power. The man's hand holds a portion of the stone's momentum; that portion is spent in tearing the fragments. Another part is deposited upon the floor: that part tears and fractures the floor itself. A third portion is deposited upon the roof, causing the walls to shake and the roof to open. A fourth portion may be wasted upon the air, carried away, or scattered in fragments far beyond the man's reach.

We observe this fact not mechanically, but through our senses and our reasoning about motion. We see the stones falling; we hear their sound and feel the jar of their collision against the walls. We note the effect upon objects near by. We measure the force that must be applied to stop a stone reaching the floor. We measure the force that must be applied to carry a stone to a distance where it cannot fall. Each of these observations tells us that weight is not a fixed thing but a variable one.

We may therefore conclude that weight is not a particle of substance that is always at rest, but a stream of forces that varies in intensity according to the nature of the body that bears it.
```

## R107

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
You have touched a matter I have long debated, and I am inclined to answer it in the same way a man would answer it: there is indeed a peculiar sensation of being pressed back into his seat, though no conscious effort compels us to move our body in that direction.

I would go further than this: we are not conscious of ourselves during our fall; we are simply pushed back, as one might thrust a hand against a door-post. This sensation of being pressed backward is not a thing we can deny ourselves, nor yet a thing we choose to resist. It is instantaneous, mechanical, and we cannot help feeling it. The motion carries us along with it.

Moreover, I find myself inclined to suppose that this same sensation of being pressed back is what we experience when we fall from a height. We are not conscious of ourselves during the fall; we are pressed forward by some force we cannot resist. The same mechanical principle applies: a falling body is pushed forward by whatever acts upon it at every moment of its descent.

I am inclined to conclude, therefore, that a man in a closed carriage, falling freely, does not feel his own weight during his fall; he is pushed forward by some force we cannot resist, and it presses him backward.

This explains why we see him so often in such cases, suspended on the doorhandle or his own feet, or falling from a window on a carriage roof. The motion itself carries him forward as a whole, and no effort of his body is required to maintain or to alter that motion. We do not feel this; we are pushed forward by our own inertia.

We may conclude, therefore, that a man who falls freely and truly reaches the ground without struggle or effort is not conscious of his own weight during the fall. He is pushed forward by some force we cannot resist, and that push acts upon him with precisely the same force that a carriage or a height causes it to act upon us.
```

## R108

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
You have touched a matter of considerable interest, one I have long suspected -- that the body of our planet Uranus is not wholly subject to the same rigorous gravitational pull as the planets nearest to it.

I am inclined to think that Uranus is not a fixed or immutable point in its orbit alone. Rather, we find ourselves in a region where the influence of other bodies -- and particularly the vast atmosphere of our heavens -- exerts a disturbing pressure upon the body's direction. It is not merely the attraction of the sun upon the body that compels it toward our system. The atmosphere presses upon it, and I am inclined to believe this pressure exerts a considerable force of displacement.

We have evidence enough that the same influence operates elsewhere within our firmament -- at Jupiter, at Saturn, at every remote star we can observe. The astronomer who watches the planet's course finds that it does not present a uniform direction throughout its journey.

I am convinced that we witness something analogous to what we observe with regard to the Moon's motion -- we find that irregularities in her approach to the Earth are reflected far more widely. The same planet's body may sweep through a greater arc as the atmospheric pressure varies, and we find the same irregularities of behaviour. It is not merely the sun's attraction alone that governs Uranus's movements; we see something more formidable: a multitude of forces acting upon it across the heavens.

I am inclined to think that the atmosphere of our system -- vast, restless, and ever-active -- influences our planet's position upon our globe. It strains its direction from the same line we observe in Uranus, and compels us to suspect that this strain is transmitted across vast distances, shaping our planet's course accordingly.
```

## R109

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
You have touched a matter of considerable importance in the science of mechanics, and I am persuaded we shall find it to be a principle perfectly universal in its operation.

I am convinced that the length of a pendulum governs the rate of its motion. A pendulum of three feet and one-tenth long swings its arc once in three seconds, whereas a pendulum of six feet and one‑tenth long swings its arc in four seconds. The same pendulum, extended to nine feet, swings in five seconds; extended to sixteen feet, it swings in eight seconds. Thus we learn that the length of the pendulum determines the time of its swing.

This principle extends far beyond the pendulum: it governs all other bodies of matter suspended in motion. A rod of lead or timber suspended at a hundred feet from its point of support moves its swing in the same period that a pendulum of one inch moves its swing. We see, therefore, that the magnitude of a body's velocity is proportional to the square of its distance from its point of support.

Moreover, we find that the same body, moving through equal distances in equal times, will acquire precisely the same velocity. A pendulum of one foot performs its swing in one second; one of two feet performs its swing in two seconds; one of three feet performs its swing in three seconds. Each of these measures the same velocity.

We conclude, then, that the length of a pendulum not only determines the time of motion but also determines the velocity with which a body moves through space.
```

## R110

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
A most curious sensation, I grant you. The elevator, though so graceful in its descent, becomes quite violent in its ascent. I have observed this phenomenon with considerable interest, and I find it difficult to attribute it to mere mechanics. You are sitting in a vessel of air, and the air in motion imparts a force to the vessel's surface. The elevator has simply not the means to counteract this force through its own gravity. The result is a peculiar, almost dangerous, velocity of descent. The cable breaks, the weight of the car and cargo descends with prodigious speed, and the entire apparatus assumes a character quite unlike what it would otherwise have.

What strikes me most forcibly is the peculiar character of motion that arrives at the ground. The elevator does not fall with the same gravity as the water in a canal. The water arrives at the ground with a speed proportional to the square of its distance from the source, while the elevator, being lighter in proportion, descends with a velocity that is, in fact, almost mechanical in character. The cable is not merely a mechanical contrivance; it is a living force, and every stroke of the brake produces a blow upon the ground floor of the car. This is not mere happenstance, I assure you. It is evidence of the force with which the earth itself acts upon these great vessels of iron and timber.
```

## R111

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
You have touched upon a fundamental inconsistency that the theory itself is not quite capable of explaining. The theory asserts that when light is propagated through all vibrations, the quantity of energy transmitted by a single wave of each colour is a constant quantity. If this were true, then the same quantity of energy ought to be transmitted through all possible wavelengths from yellow to red, from blue to violet. Yet the theory postulates that the energy is proportional to the square of the wavelength, and that the intensity diminishes as the wavelength increases. What is more probable is that the intensity of light varies directly with the square of the wavelength, but that the energy transmitted is not proportional to the square of the wavelength alone. The intensity of light is a function of the wavelength, but the energy transmitted is a function of the square of that wavelength. Hence the theory contradicts itself in assuming that energy of all wavelengths is a constant quantity.
```

## R112

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
You have identified a most fascinating confusion in the ordinary mind. The phenomenon you describe is indeed a common observation upon the earth's surface, yet it seems to contradict the natural laws of gravity we observe in the fall of a stone, a book, a body of water. The answer to this difficulty lies not in the laws themselves, but in the peculiar nature of matter as it appears in ordinary experience.

When one falls from a roof, the body of one falls with a certain velocity. The body itself is not drawn up. It is merely released, or released with its own fall, from the ground. The velocity of this release depends upon the body's mass and the distance from the point of release to the ground. A thousand yards of stone falls with a velocity of roughly fifteen feet per second. A thousand yards of lead falls with a velocity of approximately twelve feet per second. Now, if the body falls from a height of four hundred feet, it has fallen with a velocity of twelve feet per second. But if the stone falls from a building of four hundred feet high, the stone has fallen with a velocity of twelve feet per second, and the lead has fallen with a velocity of twelve feet per second. The lead, being heavier than the stone, follows later, with a velocity of approximately three feet per second, and the stone follows still faster, with a velocity of three feet per second.

This is not to say gravity is a pull upon falling bodies like a string. Gravity is a force in action, not a drawing power. The stone moves forward because the earth moves downward. The force of gravity acting upon a falling body is spent in the forward motion. The forward motion is itself the effect of that force, and the body's own motion is but the natural consequence of the force's action. This is why we observe a body falling so rapidly and a stone dropped so near the earth's surface.

Now, the explanation why we observe a stone fall from a height is that the earth's attraction upon the body exceeds that of the stone's own gravity. If the stone falls from the height of a thousand yards, the earth's pull upon it surpasses the pull of its own weight, and the stone falls with a velocity exceeding that which gravity alone could impart. This is not a mysterious force, but a law of nature acting upon matter in bulk, and we cannot explain it away from the geometry of motion.

The stone does not fall from a higher ground because gravity draws it down. It falls from a lower ground because gravity draw it downward. Whether this is a force acting through space, or whether our understanding must be corrected to account for gravity itself, I cannot say. But the facts of falling and of gravity are bound together in the order of nature, and the question of why gravity draws a body downward is not a question of force but of the relation between matter and motion. Height signifies only the magnitude of the body, not the cause of motion.
```

## R113

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
How is a stone said to fall from a mast? What is the object of the sailor at the masthead? How is the stone said to "fall from the mast"? How is it said to "fall from the mast"? What is meant by "upside down," and "right side up"? How is it said that the stone is "directly under the mast"? How is it said that it is "alongside of the mast"? How is it said that it is "below the mast"? What is meant by the words "at its proper distance"? How is it said that it is "within a foot of the mast"?

What is the meaning of the words "in a line with the mast"?

What is the meaning of the words "just forward of the mast"?

What is meant by the words "at the foot of the mast"? To what is the mast "right hand"? How is the mast "left hand"?

What is meant by "right forward"? Where is the mast "left hand"? If the stone leaves the mast behind it, and falls "right athwart the mast," what will be the position of the mast when the stone has passed the mast? If the mast is right hand forward, what will be the position of the mast when the stone has passed the mast?

To what is the mast "at its proper distance"? How is the mast "right side down"? How is it said that the stone is "alongside of the mast"? How is it said that it is "a foot ahead of the mast"? How is it said that it is "a foot behind the mast"? What is the meaning of the words "right forward"? How is it said that the stone is "a foot ahead of the mast"? How is it said that it is "a foot behind the mast"? When is it said that the mast is "right side down"? When is it said that it is "alongside of the mast"? When is it said that it is "a foot in a line with the mast"?

When is it said that the mast is "right side up"? How do you find where the mast is "a foot in a line with the mast"? Where does the mast lie "behind the mast"? Where is the mast "a foot behind the mast"? Where is the mast "at its proper distance"?

How is the mast "near the mast"? How is the mast "a foot ahead of the mast"? How do you find where the mast is "a foot behind the mast"? How is the mast "below the mast"? What is meant by the words "right aft"? How is it said that the mast is "alongside of the mast"? How is it said that the stone is "just forward of the mast"? How is it said that it is "a foot behind the mast"? How is it said that the mast is "a foot behind the mast"? How is it said that the mast is "alongside of the mast”?

How is the mast "below the mast"? How is it said that the mast is "a foot behind the mast"? How is it said that the mast is

DICTIONARY OF

"just forward of the mast"? How is it said that the mast is "a foot behind the mast"? How is it said that the mast "a foot behind the mast" is "right side down"? How is it said that the mast is "right side up"? How is it said that the mast is "a foot behind the mast
```

## R114

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
Your observation is most apt, and the cause lies in the very nature of the etheric medium itself. The ether, though apparently a continuous, finite substance, is in truth a composite of molecules, each endowed with a specific velocity and a particular mode of motion. When a wave of light encounters this substance, the molecules of the ether transmit their own motion along the path of the wave, whilst the ether itself possesses no motion or elasticity. The wave passes from molecule to molecule, much as a river passing through a solid obstacle does not swell into a lake, but rather yields gradually to the current, moving in a direction determined by the wave's path. When the wave meets a molecule of ether, the molecule, in turn, imparts energy to the ether, which in turn transmits it to the next molecule, and so forth. This process continues until the energy of the wave has been dissipated across the length of the ether and no longer exists.

Now, why does the ether thus possess no capacity to acquire motion or change its own form? The answer lies in the very constitution of the ether itself. The ether is not a substance susceptible to extension or compression, not capable of being compressed or extended. It is a medium whose constituent atoms are so arranged that they cannot be displaced or altered by the action of forces external to the ether itself. When a wave enters the ether, the atoms of it are set in motion, and this motion is transmitted through the medium much as a gentle breeze passes through a field of wheat. Thus, the energy of the wave is not stored in the ether but is simply transformed.

The theory of equal sharing of energy thus appears inadequate to account for the phenomena observed. Each wave of ether, when it reaches a fixed point, receives its own portion of energy, and no other wave of ether can ever acquire this energy of its own. This is not a contradiction, but rather a consequence of the law. What is true of one vibration is true of all, and the ether remains a fixed and unchangeable thing, unalterable by the very vibrations that are capable of producing light.

The true mechanism is that the ether itself cannot accelerate or retard the motion of its own atoms. It is the energy that the wave imparts to the ether that the ether transmits faithfully, not the energy that the ether itself acquired. This is why the motion of a wave cannot be doubled; the energy is all transmitted and all is reflected. The wave simply carries the energy from the source to the surface of the drop and back again without any of it being absorbed, transformed, or lost by the journey. It does not acquire heat, not grow, not change its character. It is merely transgressed from place to place in the ether. It is propagated through the ether with the speed of light, and there it breaks the path at each impact and retreats to the ether again, a motion of its own devising, but not of the ether's making. This is the mechanism of light, a motion of molecules and atoms, a motion that is transgressed and then transmitted, and transmitted again to the ether, which transmits it on with the same velocity it received from the source.

This explains the constancy of the ether's motion, for the ether receives and transmits energy without change in its nature. It is the medium through which light and heat pass. The theory of equal sharing of energy therefore fails to account for the phenomena of light, heat, or electricity, the very principles by which we explain the motion of the planets, the decomposition of minerals, and the very mechanism through which force appears. It is a beautiful simplicity, but it fails to account for the very existence of the ether itself and for the nature of the motion it transmits.
```

## R115

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
You have touched a point of considerable importance, and I am not sure we may yet entirely agree upon what we ought to think of this matter.

We are accustomed to imagining gravity as a force of a certain mass upon a body moving from a height. But this is a mistake. The body reaches the ground with no weight at all. It is the force of its release from the height that presses upon it, and it does not press upon the ground beneath it. The floor of the cabin or the earth itself is left behind, and the object drops with no burdens upon it. This is not gravity in the sense of a weight. It is a sudden, violent action.

I am inclined to think our notion of gravity as a pressing force is a mistake. The falling body does not press upon the earth's surface. It presses upon the air surrounding it, displaces a portion of that air, and carries away with it whatever particles of matter or other substance happened to be lying in its path. When a man lands from a roof, this air itself rushes in from all directions, and carries with it whatever light objects are scattered about the building or the floor of the cabin.

We observe this immediately in our own moments of falling. A man drops from a high window or from a cart upon a rough road; a carriage wheel runs over a stone pavement and carries away loose particles of sand or gravel. These particles are not carried by gravity in the same sense as a stone is carried. They are carried by the force of the collision and the change of form.

I am inclined to think we ought not confuse mass with weight, but rather consider the nature of the motion. A body set in motion by a force of release moves forever without weight. It is not a weight that draws or presses upon it; it is something quite different: a force of release, an ability to move away from its position and carry with it whatever matter or other substance lies in its path.

This is far more consistent with observation than our common notion of gravity demands.
```

## R116

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
Your observation is most apt, for the phenomenon you describe indeed reflects the delicate equilibrium of the planet's own intrinsic forces upon its orbital motion. In the case of Uranus, the forces emanating from neighbouring planets exert a pull upon it that is not uniform in direction across every part of its orbit, but rather tends to vary in proportionality to the orbital distances, as you note. This variation in direction between neighboring planets may be the very mechanism by which Uranus is drawn toward the sun, though its true path remains concealed beneath the veil of gravitation.

By Newton's law, the force of gravitation at a distance of approximately 190 million miles from the sun is proportional to the inverse square of the distance, and the acceleration of such a force is thus expressed in terms of the inverse square of the distance. The planet Uranus, by virtue of this law, is drawn toward the sun with a force that would, if left undisturbed, urge it toward the centre, whereas the sun's attraction upon gravitation would cause it to be drawn away from the centre.

The eccentricity of its orbit, coupled with the inclinations of its orbital planes, further amplifies this effect. The elliptical path would, by the operation of gravitational influence alone, be drawn into an arc of increasing curvature, hence the elliptical character of its orbit. The inclusion of these forces, one of the most consequential of planetary mechanics, renders the path of Uranus less a straight line than a hyperbolic arch.

Moreover, the planet's rotation upon its axis, particularly the inclination of its orbit to the ecliptic, would amplify these forces in a manner not unlike that of the moon's orbital motion. The sun's gravitation would thus act upon the planet with a pressure proportional to the inverse square of the distance, while the moon's orbit reflects this same law, though in a diminishing proportion.

Thus, while the precise mechanism remains elusive, the forces that bind Uranus to the sun are no mere accidental variations of the planet's own orbital motion, but the very sinews of its own existence.
```

## R117

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
Your question touches upon one of the most elegant principles in natural philosophy, and it is one upon which the mind naturally takes an attentive pleasure. The stones do not fall from the top of a tower at the same instant, for the velocity is not uniform.

When the weight at the bottom of the tower reaches the ground, it experiences not merely the loss of gravity that would have been given to a lighter body, but a sudden and complete loss of its motion. Now, the body that falls downward has not been simply brought to rest; it has been struck with considerable force. The stone at the top, by contrast, is not brought to rest by the hand of man; it is merely arrested by the stone that strikes it.

This phenomenon is not a matter of chance. When a body is struck, it is compelled to move through a certain space before it is stopped. If a stone falls from the top of a building, it will not strike the ground until it reaches a point somewhat lower than the point where it would otherwise strike the ground. The distance from the building to the stone at the point where it meets the ground measures this distance. The more stones that are brought down from the tower, the more stones will strike the ground in a definite succession, and the length of the fall will be the same.

The principle is not mysterious, though it requires patience and repeated observation. When you are standing upon a hill watching a stone fall, you are observing, with great precision, the successive motions of the stones that fell from the tower. If you had a string of pebbles beneath your feet and watched the stones strike them, you would understand why the stone struck at the tower's top reached the ground first. It is the motion itself that determines the time. The motion is not uniform, but it is uniform in the matter of time. The stones that are thrown upward do not fall with equal velocity, but with varying velocities, and their times of descent are proportional to those velocities.
```

## R118

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
is the next question. The answer is that Uranus is a mass of matter, and that the sun is its attraction, and that the two together are the cause of the planet's deviation from its orbit. This is an interesting instance of a law of nature that is found to be verified.

The fact that the sun does draw the planet towards itself is of importance in explaining the action of light. If the sun were not attracting the planet, and the planet were not attracting the sun, the sun would not be visible. The planet is therefore visible because it is attracting the sun, and the sun is visible because it is attracted by the planet. The sun is a body that is attracted by other bodies, and its gravitation accounts for the planet's apparent motion, and for the bright appearance of the sun.

The moon is a body that is attracted by the earth, and is not attracted by the sun. It is therefore evident that the sun and moon are not in the same straight line, and the sun must be a little to the right of the centre of the earth. The moon must therefore be going round the earth, and the earth must be going round the moon. A great many astronomers, however, hold that the moon rotates in a definite direction.

The moon has been found to be in a state of change, as seen by the telescope. The reason for this is that the earth and the moon are in different regions of space, at different distances from the sun, and the moon, being farther from the centre of the earth than the sun is, moves in a different direction from the earth. The earth, on the other hand, is revolving in a straight line, and the moon moves in a curve.

The earth, however, is not quite in the centre of the moon, as seen by the telescope, and the moon is therefore moving in a different direction from the earth. This is a very good illustration of the fact that the moon is round. The earth is at rest in the centre, as seen by the telescope, but the moon is in a state of motion, as seen by the eye. The moon is therefore going round the earth, and the earth is going round the moon. The axis of the moon is not straight, as seen by the telescope, but it is not in a straight line, as seen by the eye, and the moon, therefore, revolves about the axis of the earth. The earth is a globe, and the moon is a globe, and as the earth revolves, the moon also revolves. The earth moves round the sun in twenty-five days, and the moon in about three months. When the earth is at rest, the moon is in the same phase as the earth, but when the earth is in a state of rotation, the moon is in a state of revolution, and is at the same phase as the earth. As the moon is round, it is evident that its orbit is not round the earth, but that it is in the same phase as the earth.

The motion of the moon is not uniform, but is subject to irregularities called tides. At the full of the moon, the tide rises at the

EQUA TUDE OF THE TIDES.

253 equator and falls at the poles. The greatest tide is called the

Neap Tide, because it occurs about the time when the moon is at the greatest distance from the earth. The least tide is called the

Flood Tide, because it occurs at the time the moon is nearest the earth. The time of the new moon is called the Last Quarter, and the time of the full moon the First Quarter. The new moon is also called the time of the Full, because the greatest tide is at the time the moon is at
```

## R119

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
You have touched a most vexing question, and I am convinced it is one we have not yet properly understood.

When a body descends from a height, we are not supposed to ask whether it presses upon the ground beneath it. We reason from our experience of bodies falling to the earth. We judge by the weight of the body, and from our observation of the manner in which it falls. We speak of weight as an active force pressing upon the ground.

Now, I have little patience for this notion of our bodies exerting a continual pull upon the earth. We do not. We do not observe it. We are reasoning from our experience of falling bodies. A stone dropped from a height does not drag upon the ground. It proceeds with its own force of motion and descent. The weight is not a passive burden.

I am persuaded that we ought to seek other explanations. We ought to consider that gravity operates according to its most general laws, not our particular measurements of the body's weight. We perceive that bodies fall, that they move toward the ground, that they cease to support themselves and fall freely. This is not a pull, but a motion.

I am convinced we ought to recognize that gravity operates not as a constant weight pressing upon the earth, but as a principle of action and motion itself. The falling body does not feel its weight; it moves with its own force of motion and descent. It is not the body that bears the burden, but the body that moves with its own force.

We ought then to acknowledge that the body's motion represents not a constant pull upon the ground, but rather a universal operation of force. It does not press upon the earth in an unseen manner; it acts upon whatever objects it encounters, moves them, and carries itself along with them. The weight is not a chain pulling upon the ground; it is the body's motion and its own energy of descent.

This distinction I find invaluable: we mistake our experience of weight for our explanation of gravity's operation.
```

## R120

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
You have touched a matter of considerable importance, and I am persuaded that such an experiment proves nothing more than vanity dressed in scientific costume.

Observe: when a stone falls, it does not descend perpendicularly. It does not drop along a straight path. It descends at an angle of forty-five degrees, and this angle is no accidental thing. The stone descends precisely at that precise angle; no other direction suits its nature. We are not measuring the fall by a straight line; we are measuring the angle at which the body descends.

Now, suppose that two stones were let fall from the same height, one ten times larger than the other. The heavier stone reaches the earth at precisely forty-five degrees before the lighter one commences its flight. The lighter stone strikes the ground at precisely the same angle. This is not a coincidence. It is a law of nature written in the very architecture of gravity.

I am persuaded that we ought not measure the descent of our bodies by the straight path of a falling body. The descent is determined by the angle at which gravity acts upon a body. A man walking at a modest pace, and seeing a stone fall from a height, will not construct a straight path of eighty or ninety feet. He will draw from the body an angle of forty-five degrees and allow for that angle to carry him down. The body obeys its law. We observe this not in our individual exertions, but in the operation of heavy bodies at different inclinations.

We may conclude therefore that our bodies do not descend perpendicularly, and that our fall is governed not by a level line of descent, but by the angle at which gravity acts upon us. The heavier stone reaches the ground at a different angle, and we observe that angle in the direction of its descent. The lighter stone does not fall perpendicularly; it descends at the same angle, and strikes the ground at precisely forty-five degrees. This is no accidental coincidence; it is the law of gravity operating upon our terrestrial bodies.
```

## R121

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
You have touched upon one of the most vital questions in natural philosophy, and I am pleased to say the matter is rather more straightforward than it might at first appear. The difference you observe between the direction of a ray and the direction of its motion is not a matter of mere optical illusion, but rather reflects the very nature of light itself.

When light travels from a luminous body to our eyes, it proceeds in a right line. This is not a whim of optics. We have discovered, through patient experiment and careful observation, that the rays themselves are propagated in directions which are straight and perpendicular to the surface of the medium through which they pass. This is not a mere convention of optics. It is the fundamental principle of light itself.

Now, when the Earth turns its axis in the direction of its rotation, the direction of a ray of light differs with the angle it makes with the Earth's surface. A ray directed toward the pole of the Earth moves in a direction parallel to the Earth's axis, because the Earth rotates eastward and westward about its axis. A ray directed toward the equator moves in a direction perpendicular to the Earth's axis, because the Earth itself is turning through an angle of approximately ninety degrees.

The reason for this is quite simple. When a particle of light is passing through water, or through a transparent medium, it moves in a plane which remains fixed in space. But when light passes through air, or glass, or a medium of any other nature, it meets a new surface. When a ray of light passes through water, it strikes the surface at an angle, because the surface of water is inclined to the Earth's surface. When light passes through air, it strikes the surface at an angle of forty-five degrees, because the surface of a sphere is inclined toward the Earth in that angle.

Now, this angle is precisely the angle at which the ray meets the surface. If the surface is at an angle of twenty degrees, the ray would strike it at a right angle; if it is forty-five degrees, the ray strikes it at ninety degrees. The two angles are together equivalent to the right angle. Every ray of light, therefore, passes through the same angle when it travels through the same medium.

So the direction of a ray in space is fixed, because the direction of the Earth's motion is fixed. The directions are not absolute. They are merely relative to the particular medium through which the light travels. It is the Earth's motion that determines the direction of the ray in space, and it is the angle at which the ray strikes the surface that determines the direction of the ray's own motion.

This is not a mere mathematical curiosity. It is the fundamental principle of optics. It explains why sunlight, reflected from a mirror, follows the same direction as an eclipse of the sun, and why the refracted light of a luminous body appears to move in a direction contrary to the direction of the source. The law is universal, and the principle itself is established by experiments and observation. It is one of the most elegant, if somewhat paradoxical, truths in natural philosophy.
```

## R122

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
You have touched something essential to our present understanding of gravity and the nature of bodies falling free.

When we observe the descending weight drop without consequence, our senses assure us it is nothing. The scale's index does not register this; it is a signal of the force with which the falling body strikes the floor. We record this force through the movement of the weight's descent. We observe the velocity with which it passes through the floor or along the platform; we determine the distance it falls, for we measure the magnitude of the impulse.

Now, here is the crux: we find this impulse altered by the nature of the body itself. A stone deposited from a height by gravity will not fall in a vacuum; it will strike the ground with a certain definite velocity. If we add this velocity to the weight, we obtain a different result from the same force. The scale tells us this: the stone's moving mass exerts its force upon the machine, and the force is less than what it would have been had we left it quiet upon the platform.

We thus learn that the weight does not simply hang motionless upon the beam; it exerts a measured pressure upon the floor and its support. This pressure is measured by the distance the body descends from its initial position. The scale records this distance, and we may read it as the magnitude of the force expended.

We do not measure this force by merely weighing the matter; we measure it by observing the work it accomplishes. A man falling from a height exerts an energy equal to the weight raised. This energy disappears or is transformed into motion, and that motion is proportional to the square of the falling body's mass and the height from which it descends.

This principle governs our investigations into the action of gravity upon bodies. It tells us we must not measure a body's weight by the weight alone. we must know how that weight acts upon the support of the framework and the matter of the body. The scale thus becomes an instrument of measurement, not merely of force measured by the balance or the spring.

We may then conclude from this observation: a body in motion exerts upon the mass of the support a force proportional to the square of the velocity it acquires. This is the law of gravity: the energy exerted is proportional to the square of the velocity acquired. It is no accident that we find this true; it is a universal principle we may apply with confidence to all bodies falling under similar circumstances.
```

## R123

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
What in special?

Explain the phenomena in regard to the human body.

If a man falling in a roof were to find a narrow space just above his head, and were to fall through it, and if he were to feel the air pressing upon his chest, and his face turned toward the ceiling, would be be likely to be hurt by the impact of the roof upon his head?

What is the sense of weight? What use is made of it? What do we mean by the expression "weight of a thing"?

When a man falling from a roof meets an object which may be pressing upon him, and which he may be unable to avoid, what is the first thing he thinks about?

What happens if a man is caught by a roof?

Is it not better in such cases to get down as quickly as possible?

If a man is caught by a roof in a closed space, what may be the result?

What is the condition of a man who is caught in a closed space, where he can make no effort to escape?

Why is it better to get out of the way of a roof?

What is the condition, then, of a man who is catching himself by his hands, or by his feet, or by some part of his body?

What is the condition of a man who is caught by a roof?

What would be the condition of a man caught by an open space?

If a man is catching himself by his hands, is it not safer to let go of his hands?

What if he is caught by his feet?

If a man were caught in a closed space, what would be the first thing to be done?

What would be the second thing?

What if he were caught by his feet?

What would be the third thing?

What if he were caught by his hands?

What would be the fourth thing?

What is the condition of a man caught by a roof?

What is the condition of a man caught in a closed space?

What is the condition of a man caught in the open air?

How are persons caught in a closed space usually caught?

How do persons catch themselves in a closed space?

If a man is caught by his feet, is it safe for him to kick?

If he is caught by his hands, is it safe for him to strike?

What is the condition of a man caught by his hands?

If a man is caught by one of his hands, is it advisable to let him go?

If a man is caught by his hands, is it advisable for him to attempt to get out?

What is the condition of a man caught by his hands in a closed space?

What if he is caught by his feet?

What if he is caught by his feet?

What other condition is necessary to success?

What if a man is caught by his hands and feet?

What if a man is caught by his feet and hands?

What if he is caught by his feet and hands?

What if he is caught by his feet and hands?

What is the condition of a man caught by a roof?

What is the condition of a man caught in a closed space?

What is the condition of a man caught in a closed space?

What is the condition of a man caught in the open air?

What is the condition of a man caught in the open air?

What is the condition of a man caught by his feet?

What is the condition of a man caught by his feet?

What is the condition of a man caught by his hands?

What is the condition of a man caught by his hands in a closed space?

What is the condition of a man caught by his hands in a closed space?

What is the condition of a man caught by his hands in the open air?

What is the condition of a man caught by his hands in the open air
```

## R124

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
Your question touches upon one of the most fascinating yet vexing problems in natural philosophy, and I am glad you have raised it, for the answer lies not in mere mathematical calculation but in the very constitution of our bodies and the forces that animate them.

The stone that falls from the top of a tower descends from a height of some two hundred and fifty feet, and carries with it a tremendous momentum. Now, if a body of ten times the mass had been placed upon the earth at that same instant, the stone would have been met with ten times the force, and both would have descended together, with the stone falling through a distance of roughly one hundred and fifty feet. But the stone that falls from the tower strikes the earth at a distance of nearly one thousand feet from the tower's foot, and therefore loses nearly one half of its momentum.

The loss of momentum is not merely a matter of speed. It is one of the principal forces that drives all our machines. The stone that falls from the tower has spent a portion of its momentum in producing motion and in generating mechanical energy. This energy is then stored up in the stone and passed on to the other falling body, which, in turn, acquires momentum from the same energy. The stone that falters and the stone that lands with its full momentum are not the same body, and the momentum of the former is very much greater than the latter.

This principle explains why a stone upon the ground, when at rest, does not immediately fall, and why a body descending from a height does not attain the speed it ought to acquire from the initial momentum. The momentum is not fully absorbed in the first instant, and it spreads around the body like a faint wave. The stone that falters loses a great deal of the energy it might otherwise have expended in velocity and work, and the stone that lands with its full momentum, having absorbed all momentum from the fall, reaches the ground with a speed that has never been fully reduced.

This principle also explains why the sudden descent of a stone from a height produces such violent effects, such stunning pain, and such devastating effects upon the living. The momentum it carries is not dissipated in the air, but is retained in the body itself and then acts with a force that is quite beyond what the body alone would be capable of producing. This is why the falling stone, when it strikes, produces a blow that is both painless and dangerous, and why the shock of a sudden blow can kill a man at once.
```

## R125

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
Describe a common experiment with the falling body. What do you know of gravity?

What is the effect?

What do we learn from experimenting with the falling body? What is the effect of the falling man or animal upon a third person? How do we know of the effect upon the man and animal?

What is the effect of a heavy falling body upon us? How do we know that a body falls freely? How do we know that it is heavy?

What do we know of the nature of gravity? What do we know about gravity in general? What follows about gravity from experimenting with the falling body? What do we know of the nature of gravity from the effect of gravity upon us? What do we know of the nature of gravity from experimenting with the falling body?

What inference do we draw from the effect of gravity upon us?

What is the inference from the effect of gravity upon the falling body?

What, then, do we draw from the effect of gravity upon the falling body?

CHAPTER III.

THE FALL OF A GREAT HEIGHT.

THE falling of a great height gives us the experience of a very rapid fall of the body in the air. The nature of the falling body is such that the falling body is made. to strike very deep into the air, and this causes the body to move with a great velocity.

This is the manner in which a great height is overcome.

A great height is overcome by the shock of an immense. body falling from a high height.

The velocity of a body falling from a high height is greatest in proportion as the body falls through the space through which it is falling.

If the body falls through a space where it is not falling, it is still a great height; if it falls through the space of a whole atmosphere, it is a great height; if it falls through the space of 18 miles, it is a great height.

The velocity of a falling body is also greatest when the body falls through the air, but is not in contact with the air. A body falling through the air does not need to touch the air in order to fall through a great height.

It is the same in falling through a great distance; a body falling through an immense distance does not need to touch the air in order to fall through a great height.

The body which falls from a height is the shock of its own motion.

The shock of the motion of a heavy body falling from a high height is very great. If a body falls from a height, it is in the air, and there is no reason why it should not fall directly to the ground; a great shock of motion, however, causes the body to descend; it is in the air, and there is no reason why it should not descend. The body moves forward, and the shock of motion causes it to fall very rapidly; the body descends, and the shock of motion causes it to descend very rapidly.

The shock of motion of a falling body is very great.

The velocity of motion of a falling body is greatest in proportion as the body falls through the space through which it is falling.

If the body which is falling strikes the air at the bottom of a deep valley, it is very likely to fall upon a rock or stone, and there is no reason why it may not strike the rock or stone, and thus fall through a great height. If, however, the body strikes the air, it is likely to fall upon a rock, and there is no reason why it may not fall upon a rock.

A great body falling through a great height is almost a constant condition of a great height.

The shock of the motion of a falling body is greatest in proportion as the body falls through the air; hence, if the body falls through the air, it is almost equal to a great
```

## R126

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
You have touched something very terrible indeed, and one I have observed with great frequency in my travels through the cities of Europe and America. The sudden rupture of a cable produces a shock that is not confined to the immediate moment of release, but extends far beyond the spot where the mechanism gave way.

I have witnessed men knocked down by this catastrophe cry out in their terror, fall upon their knees in despair, and then roll about the floor in a state of complete bewilderment. The shock runs through the whole system instantaneously, and the brain and spinal cord feel it with terrible force.

I have seen men of middle years and stout constitutions reduced to crying children, their limbs trembling like reeds in a gale, unable to stand upright. I have heard of cases where a man who had walked a mile or two in perfect health has carried himself home with a crick in his neck or a numbness in his limbs for days or weeks. The shock acts upon the nervous system with particular severity.

I have heard of other cases wherein men leap from windows, leap from tops of high walls, leap from trees during the fall, striking their heads upon stone or ground in their haste. These things are not accidents of nature, but consequences of the rupture itself. The cable gave way, and the weight of the elevator and its cargo falls upon our heads with particular severity.

I suspect we do not sufficiently consider the danger of such shocks when we stand in an open elevator with our heads turned away from the falling mass. The shock operates upon us with considerable force and produces effects we might not anticipate. It renders our nervous system more susceptible to injury, and our body to disease. It is a species of catastrophe we ought never to encounter again without considerable caution and preparation.
```

## R127

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
You have touched a matter I have long debated, and I find myself in agreement with Mr. Whewell's view that light does not move in a direction perpendicular to the Earth's motion, but rather proceeds along the line of motion itself. This is no fancy notion of astronomers working by observation alone; it may be verified with a simple experiment.

Lay a sheet of paper upon a table and place a candle flame upon a distant projection of the paper. Draw a ruler through the flame and the projection, and you will find the candle illuminated upon the other side of the table, not upon the same side of the paper as the flame. This is not a random coincidence; it is a universal effect: the light is always in the direction of motion.

I have verified this again and again with various apparatus. I have turned the mirror of my telescope to the same point of the firmament, and the image of the distant stars was always in the direction of the Earth's motion. I have turned the second mirror at a quarter right angle, and the image was not moved at all, but remained precisely where the first mirror had placed it.

A ship's hull is being passed through clear water, and the water itself remains unchanged. The sailor does not shift his position; he is moved by the motion of the vessel. This reasoning is not fanciful; it is backed by careful observation and experiment.

I find myself in agreement with Mr. Whewell's conclusion: the two speeds are not opposed but in harmony, and the motion is not perpendicular to the direction of light. The light moves in a direction along the Earth's motion, and its speed is not altered by this motion.
```

## R128

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
Your observation strikes at the very heart of motion's law. In the first case, the object falls with an accelerating velocity, and the mind registers its movement as a force that acts upon the body, not the body upon the mind. The weight, as we call it, merely follows the body's motion, yet the mind feels it as a force that acts along the motion. In the second case, the object is not pressed down into the seat, but merely thrust back upon it; the motion of the body may be as swift as it pleases. The mind, by analogy, does not feel the body being thrust forward, but rather is drawn backward by its inertia.

Now, why does the body not feel the weight of falling bodies? The answer depends upon the nature of the body and the velocity of its motion. A body moving with a moderate speed -- say, a mile per minute -- carries its own weight at that rate, and the mind may not notice this save in a moment of great peril. But if the body moves at such a pace that its weight approaches a mile per minute, the mind feels the weight of the fall as a force upon the ground. The body becomes what the French call a "dangerous" object.

Consider this: when a carriage is pulled forward with ever-increasing speed, a person in it feels the motion as a force pressing backward. This force is not felt, for the body has already moved beyond the seat. The mind simply finds itself drawn backward, and the body itself is not the mechanism that pulls it; it is the inertia of the matter. The man who falls freely from a roof feels no weight pressing back upon him, because his own motion already carries him past the seat.

The danger in falling from a high carriage is even greater than from falling from a roof; for the roof permits the body to move forward, yet the floor beneath our feet offers no resistance to the velocity with which a carriage may be dragged. The body, once the carriage has acquired its motion, does not fall upon the hard ground, but rather glides past it with the speed of the carriage itself. It does not feel the floor in motion; it feels the floor in motion.

There is also the matter of distance. A carriage that moves at a speed of several miles per hour can move a small man a fraction of a mile at a time, and the distance is the square of that time, not the square of the speed. The mind, therefore, may still feel the weight of falling bodies moving through space, though the physical motion that carries them is vastly greater than its own rate of motion. The difference between a freely falling body and a body moving at a high speed in a closed carriage, however, is one of magnitude rather than nearness. It is that difference that makes the peril of falling so grievous, and makes a danger so readily recognised by those who have witnessed it. Seek to walk or ride with the speed that nature itself demands, and the weight of the fall will not burden you.
```

## R129

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
You have touched a matter of considerable importance, and I am pleased to offer my thoughts upon it, for this is a subject I have lately examined with some interest.

I am persuaded that the pendulum's length does not merely determine the duration of its oscillation. It governs, and in many cases supersedes, the velocity of the oscillation. A heavy body of two feet in length reaches its terminus in the same interval as a lighter one of one foot. The longer the pendulum, the slower the swing; the shorter the one, the swifter the motion.

This rule applies equally to bodies of other dimensions. A pendulum one foot in diameter vibrates twice as swiftly as one of nine inches; one of four feet vibrates four times as swiftly. The relationship is not arbitrary; it is constant and immutable. We may then conclude that the length of a body's pendulum governs not merely its duration, but its speed of swinging.

I find this conclusion exceedingly instructive. It suggests that we must not seek a single, unvarying principle in nature, but rather a balance of forces and variation. A great body vibrates more swiftly than a small one; a slow one vibrates more swiftly than a swift one. The same body vibrates in different times according to its distance from the centre of suspension or according to the weight it bears.

I am persuaded, therefore, that we ought not measure a pendulum merely by its length, but by the proportion which its length bears to its mass and its weight. A pendulum of two feet in length carries twice the weight of one of three feet, proportionally. This is not a mere coincidence; it reveals a principle of considerable importance to our reasoning about the pendulum.

We may then state our conclusion: the length of a body's pendulum is not a mere coincidence; it governs the motion of that body, and it governs the velocity of its oscillation. They are not independent elements. We may therefore conclude that a pendulum of considerable length and one of measured shortness ought proportionally to affect the speed of their swing, and this proportion determines the duration of both their oscillations and our estimate of their respective lengths.

This leads us to a more precise notion: we measure the duration of a pendulum, not merely by the length of its body, but by the proportion which that length bears to the mass and weight of the body. The shorter a pendulum, the faster its swing; the longer a one, the slower its swing. This is no accident of nature. It is a fundamental truth that we must acknowledge and accommodate our reckoning of pendulum motion by observing this law: the length of a pendulum governs the frequency of its oscillation, and frequency governs both the duration of swings and the intensity of our estimation of body weight or velocity.

We may, I think, conclude with confidence that a pendulum of a foot or two in length measures its oscillation by this proportion: two feet swifter than one, four swifter than two, sixteen swifter than two. This is not an arbitrary arrangement; it is a law written in the very constitution of bodies and the motion of bodies connected with that law.
```

## R130

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
You have touched a matter of considerable importance, and I am inclined to think the explanation I gave you is not quite sound.

You must understand that we measure energy not by the whole of it at each level, but by the proportion of it expended at each level. When a body heats, you have not all exhausted at once. Each vibration strikes the particle and is reflected, refracted, or absorbed; some of that energy is wasted altogether, lost in heat, or in doing work upon the body itself. The energy that is not wasted rises to a height at which it can do work.

Now, according to this theory of equal sharing, we ought to expect this: every vibration that strikes the particle, every heat reflected from that particle, and every heat absorbed by the body's own change of temperature should increase equally in energy after each interval of frequency. We should find that bodies whose temperatures differ by equal amounts will also differ by equal amounts in energy stored in them at each frequency. The particles of a red-hot stone will not receive more energy than those of a cold one; the two will share the same amount of energy.

This is contradicted by observation. A heated body appears to lose energy at every frequency, not all at once. So does a solid body of different temperaments: one of iron and another of clay or wax. The iron and the clay differ in their specific capacity for heat, and that difference determines whether the iron will part with its energy at all.

I am inclined to conclude, therefore, that energy is not distributed uniformly like a river of water, but is dissipated in different proportions according to the nature of the vibration and the body's temperature. The theory of equal sharing is not a universal principle; it is a deficiency in our present understanding of heat's behaviour.

We must therefore abandon it entirely and adopt a different conception: we find energy not in a uniform stream but in proportional quantities, and this tells us something we cannot yet fully account for: energy is not exhausted every time the vibration strikes, but is dissipated according to the differing capacity of the body to receive or retain that energy.

This distinction matters enormously for our understanding of heat's character and its mode of operation.
```

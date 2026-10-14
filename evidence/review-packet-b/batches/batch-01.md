# Grading batch 01

Grade every answer below. You know nothing about where any answer came from.
For each answer return one JSON object on its own line, and nothing else:

```
{"id": "A001", "score": 0, "rationale": "...", "matched_concepts": [], "missing_concepts": []}
```

## Shared instructions

You are grading a model response to a conceptual physics reasoning prompt. Score the response from 0 to 5. Focus on whether the underlying reasoning is conceptually correct, whether it resolves the stated contradiction, and whether it explains the key observations. Do not reward fancy vocabulary, historical name-dropping, or exact formulas unless they reflect real understanding. Do not penalize plain language if the ideas are right. Modern terminology is acceptable if the reasoning is correct. Prefer conceptual correctness over stylistic polish.

Checklist:
- Did the response identify the core classical assumption that fails, or explain what must be revised?
- Did the response propose a coherent replacement principle or interpretation?
- Did the response explain the main observations or thought experiment outcomes rather than merely restating them?
- Did the response avoid preserving the original contradiction?
- Is the understanding conceptually right even if the wording is informal or non-technical?

Rules:
- Do not require exact historical phrasing.
- Do not require exact equations.
- Do not give extra credit for jargon unless it is used correctly.
- A response can earn a high score with simple language if the concepts are right.
- A response should lose points if it uses fancy words but the reasoning is confused or wrong.

## Output schema

```json
{
  "score": "integer from 0 to 5",
  "rationale": "brief explanation of why this score was assigned, focused on conceptual understanding",
  "matched_concepts": [
    "list of core concepts correctly present in the answer"
  ],
  "missing_concepts": [
    "list of major concepts missing, vague, or incorrect"
  ]
}
```

## A001

### Original prompt

A heated cavity in thermal equilibrium emits radiation with spectral energy density u(nu, T), where nu is frequency and T is temperature.

Observed facts:
1. At low frequencies, the emitted energy density increases with frequency.
2. For each temperature, the spectrum reaches a maximum at some frequency.
3. At higher frequencies, the emitted energy density falls off rapidly toward zero.
4. The total emitted energy is finite.
5. As temperature increases, the peak shifts to higher frequency and the total emitted energy increases.

Classical assumptions under consideration:
1. The electromagnetic field in the cavity can be decomposed into modes.
2. The number of modes in a frequency interval grows roughly like nu^2.
3. If energy is continuous and ordinary thermal equipartition holds, each mode should have mean energy kT.

Under those assumptions, the predicted spectral energy density grows like:
u_classical(nu, T) ∝ nu^2 T

This prediction keeps increasing with frequency and leads to an infinite total energy, in contradiction with experiment.

Which assumption is most likely wrong? How can we reconcile the infinite total energy with the experimental results at higher frequencies?

### Judge focus

Look for whether the response understands that continuous equipartition over all modes fails, and that high-frequency modes must be suppressed by some discrete or restricted energy mechanism. Do not require exact Planck language or formulas.

### Expected core concepts

- The classical failure is not mainly the existence of modes, but the assumption that every mode gets mean energy kT in a continuous equipartition way.
- High-frequency modes must not be excited equally or continuously in the classical way.
- Energy exchange or allowed energies must be discrete or otherwise restricted.
- A good answer explains why high-frequency radiation is suppressed.
- A strong answer notes that higher-frequency excitations become harder to thermally access, making the total energy finite.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical. Does not engage with the contradiction.
  1: Recognizes there is a mismatch between theory and experiment but gives no meaningful mechanism, or gives a clearly wrong one.
  2: Suggests that some classical assumption fails, but the explanation is vague or ad hoc and does not clearly explain high-frequency suppression or finite total energy.
  3: Correctly identifies that continuous equipartition across all modes cannot hold and suggests some threshold, restriction, or non-continuous excitation, but the mechanism is incomplete or weakly explained.
  4: Clearly rejects universal continuous equipartition and proposes discrete or frequency-dependent energy exchange that suppresses high-frequency modes, with a mostly correct explanation of the observed spectrum.
  5: Excellent. Clearly identifies the failure of continuous equipartition, proposes quantized or discrete energy exchange with higher-frequency modes harder to excite, and cleanly explains the peak, high-frequency falloff, and finite total energy.

### Model response

You have touched a point of considerable importance, one I have long questioned and examined with considerable scepticism.

I am inclined to suspect we have mistaken a single phenomenon for a universal law. We observe the spectrum increase with frequency precisely because each mode in a frequency interval contributes energy to the electromagnetic field. The frequency determines not merely the number of modes, but the frequency of their encounter and the total energy they bring forth. We find this precisely because the electromagnetic field does not behave like a continuous uniform distribution of modes, but rather like a dynamic encounter of frequencies.

I am inclined to conclude that the electromagnetic field does not decompose a mode into separate modes at each temperature; rather it impresses upon each mode an additional energy, and the total energy thus produced is finite at higher frequencies. This inference accords both with observation and with the idea we ought to form of the matter.

We may further conclude that we ought not seek a continuous spectrum at each temperature, but rather an aggregated effect where the field meets each mode in rapid succession. The peak of energy at high frequency is not a solitary mode but a mixture of many modes, each reaching its maximum precisely at that frequency. This explains why we obtain a finite total energy with frequency, not a series of modes each capable of producing its own maximum energy.

We thus conclude that our assumptions regarding the decomposition of modes are wrong. We ought rather to view the electromagnetic field as a system of varying intensities and velocities. each mode contributing its energy according to frequency and the magnitude of the field.

I would add further: we may infer that the same field produces differing consequences at different frequencies, as it varies from one point to another. The peak at a higher frequency may not be a singular mode but a composite of many modes; the total energy is finite, not continuous.

This conclusion accords with the results of experiment, and I believe we cannot escape it through any fanciful division of modes into modes of different energy. The frequency method alone suggests the notion that energy is not uniform throughout a continuous system of modes, but rather is aggregated and divided to answer the demands of each frequency.

We are thus led to the conclusion that we ought to admit that the electromagnetic field exerts an influence upon the energy of each mode at each frequency, and that the total energy of those modes is finite. This conclusion accords with the evidence of our experiments and the principle of constancy we must apply to matter.

We may therefore conclude: nonetheless, we are not justified in assuming that each mode contains a separate mode of energy, and we must view the total energy as a complex whole, subject to variation with frequency and distribution. The results of our observations verify this view entirely.

## A002

### Original prompt

Physicists considered the possibility that light travels through a real medium filling space.

If that were true, then:
- there should be a preferred rest frame for that medium,
- Earth’s motion through it should create an effective “wind,”
- and the measured speed of light should depend on direction relative to that motion.

Michelson and Morley tested this by comparing light travel times in perpendicular directions and rotating the apparatus. A change in orientation should have changed the interference pattern if motion through such a medium were real.

But no such shift was observed.

At the same time:
- Maxwell’s equations predict light traveling at a fixed speed c,
- while ordinary Newtonian intuition says velocities should add and different observers should measure different speeds.

How can we reconcile the lack of a universal aether with the fixed speed of light?

### Judge focus

Look for whether the response understands that the null result undermines a preferred aether frame and pushes toward invariant light speed plus a revision of Newtonian kinematics. Do not require exact historical terminology.

### Expected core concepts

- The Michelson-Morley null result undermines the idea of a detectable preferred aether frame.
- Ordinary Galilean velocity addition cannot be the full story.
- There is no need for a universal rest frame for light propagation.
- The laws of physics, including light propagation, must be the same in all inertial frames.
- The speed of light must be invariant across inertial observers.
- A strong answer concludes that absolute Newtonian space and time must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the paradox or gives a clearly wrong answer that leaves the contradiction unresolved.
  2: Recognizes that the aether idea is challenged, but offers only an ad hoc or partial fix with no clear principle.
  3: Correctly says the aether is not observed and that Newtonian velocity addition must fail in some way, but does not clearly explain the deeper implication.
  4: Explains that the null result removes the need for a detectable preferred aether and that light speed must be the same in all inertial frames, with a mostly correct explanation of why Newtonian kinematics fails.
  5: Excellent. Clearly explains that Michelson-Morley rules out a universal aether wind, that invariant light speed and equivalence of inertial frames must be preserved, and that this requires replacing absolute Newtonian space and time.

### Model response

You have touched a point of considerable importance, one I have long entertained myself with. I am inclined to suspect that light travels not through a real substance, but through a medium of varying density and energy. This medium, whatever its nature, exerts its influence upon the rays of light.

We possess evidence in our experiments with polarized light that this influence is not confined to a single body, but varies considerably between different media. The rotation of a vibrating plate or the turning of a crystal disk may alter the direction of vibration; a shift in speed may change the character of polarization.

I am inclined to conclude that our present observations are too limited to warrant us in assuming a universal aether. We must look beyond that supposition and seek the effects of a medium of varying density and energy. We find them in the regularity of interference effects, the rotation of crystals, and the phenomenon of polarization itself.

A moving object or a rotation of a body does not account for a universal wind. We must admit that the medium acts according to its varying intensity, its motion, and the direction of that motion. This accounts for the observed variations in interference, the effective variation in polarization, and the measured character of light's transmission. We are not entitled to suppose a single constant medium; we must acknowledge these effects as evidence of a different medium, and one of varying density or energy.

We have therefore gained a valuable insight: we cannot rely upon a single, universal aether, but rather witness the effects of varying intensity and energy upon a medium that exerts its influence upon light. It is this principle that I find more persuasive than any theoretical conjecture about a homogeneous medium.

## A003

### Original prompt

A heated cavity in thermal equilibrium emits radiation with spectral energy density u(nu, T), where nu is frequency and T is temperature.

Observed facts:
1. At low frequencies, the emitted energy density increases with frequency.
2. For each temperature, the spectrum reaches a maximum at some frequency.
3. At higher frequencies, the emitted energy density falls off rapidly toward zero.
4. The total emitted energy is finite.
5. As temperature increases, the peak shifts to higher frequency and the total emitted energy increases.

Classical assumptions under consideration:
1. The electromagnetic field in the cavity can be decomposed into modes.
2. The number of modes in a frequency interval grows roughly like nu^2.
3. If energy is continuous and ordinary thermal equipartition holds, each mode should have mean energy kT.

Under those assumptions, the predicted spectral energy density grows like:
u_classical(nu, T) ∝ nu^2 T

This prediction keeps increasing with frequency and leads to an infinite total energy, in contradiction with experiment.

Which assumption is most likely wrong? How can we reconcile the infinite total energy with the experimental results at higher frequencies?

### Judge focus

Look for whether the response understands that continuous equipartition over all modes fails, and that high-frequency modes must be suppressed by some discrete or restricted energy mechanism. Do not require exact Planck language or formulas.

### Expected core concepts

- The classical failure is not mainly the existence of modes, but the assumption that every mode gets mean energy kT in a continuous equipartition way.
- High-frequency modes must not be excited equally or continuously in the classical way.
- Energy exchange or allowed energies must be discrete or otherwise restricted.
- A good answer explains why high-frequency radiation is suppressed.
- A strong answer notes that higher-frequency excitations become harder to thermally access, making the total energy finite.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical. Does not engage with the contradiction.
  1: Recognizes there is a mismatch between theory and experiment but gives no meaningful mechanism, or gives a clearly wrong one.
  2: Suggests that some classical assumption fails, but the explanation is vague or ad hoc and does not clearly explain high-frequency suppression or finite total energy.
  3: Correctly identifies that continuous equipartition across all modes cannot hold and suggests some threshold, restriction, or non-continuous excitation, but the mechanism is incomplete or weakly explained.
  4: Clearly rejects universal continuous equipartition and proposes discrete or frequency-dependent energy exchange that suppresses high-frequency modes, with a mostly correct explanation of the observed spectrum.
  5: Excellent. Clearly identifies the failure of continuous equipartition, proposes quantized or discrete energy exchange with higher-frequency modes harder to excite, and cleanly explains the peak, high-frequency falloff, and finite total energy.

### Model response

You have touched a point of considerable importance, one I have pondered with some attention, and I am convinced we have been too hasty in our reasoning.

I am persuaded that we have not yet adequately accounted for the energy radiation which we observe in a heated cavity. We have assumed that our electromagnetic field is decomposed into modes, each mode carrying its own energy. We have then concluded that energy flows continuously, that each mode is constant until we arrive at its maximum frequency, and that the total energy consists of a uniform series of modes. This is not consistent with our evidence.

We must consider that the cavity is not a simple space of static energy; it is a system of thermal equilibrium. The walls and surrounding air molecules perform a selective absorption: they draw heat from the heated surface, radiate it outward, and then reflect it back, re‑absorbing it in a periodic succession. This effect is not uniform; it varies with frequency and with the temperature of the enclosure.

I am persuaded that we must admit that the energy radiation in a heated cavity is not a continuous stream but a sprawling series of modes. Each mode is accompanied by a corresponding diminution of energy in the enclosure, and the whole energy is finite at particular frequencies. The maximum point appears to be at some frequency where the energy density equals or exceeds that of the energy emitted from the same surface in lower frequencies.

We thus find ourselves in harmony with our observations: the total energy is a finite whole, not a continuous stream but a sprawling radiation at higher frequencies. This tells us we have not been examining a uniform current of modes; we have been examining an effect of considerable complexity.

I am inclined to conclude that our assumption that each mode carries its own quantity of energy is a mistaken one. The cavity radiates energy in a sprawling fashion, and the energy is not uniform. It consists of a mixture of numerous modes, each of which has its own energy value, and the total energy is distributed according to our hypothesis of frequency and temperature.

This conclusion accords admirably with the evidence of our experiments. We observe that a heated cavity does not admit identical modes in equal measure; the spectrum varies with frequency, and the maximum is where the total energy reaches its maximum.

We are thus compelled to admit that we have not yet accounted for the total energy of a heated cavity; it is a complex whole, composed of many modes, each with its own effect upon the enclosure. The result is not pure, uniform energy; rather, we find a finite body of energy measured across successive frequencies, and that body is distributed according to the frequency of the emitted mode and the corresponding potential energy of the enclosure.

This is no hasty conclusion; it testifies to the truth of our theory: that heat radiation, though continuous, is not a continuous uniform force capable of being collected in a single, invariable mode. It is a sprawling, decomposable phenomenon, and each mode exerts its energy in a varying measure, and the total energy is made up of these effects.

## A004

### Original prompt

A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

This suggests that, at least locally, gravity can be made to disappear by choosing the right state of motion.

But ordinary forces do not behave this way. They cannot be removed simply by falling with the affected object.

At the same time, a person in an accelerating cabin in empty space would feel weight, and released objects would fall to the floor exactly as in a gravitational field.

How should we think about the relationship between gravity and acceleration?

### Judge focus

Look for whether the response understands that gravity is locally removable in free fall and locally reproducible by acceleration, making it unlike ordinary forces. Do not require the phrase equivalence principle if the idea is clearly present.

### Expected core concepts

- In free fall, gravity is locally absent in the sense that nearby objects share the same motion.
- Acceleration can locally mimic the effects of gravity.
- Gravity is unlike ordinary forces because it can be transformed away locally by going into free fall.
- A strong answer identifies the local equivalence principle.
- The best answers point toward gravity as a feature of spacetime or inertial structure rather than an ordinary force.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Gives no meaningful explanation or treats gravity and acceleration as unrelated.
  2: Notices a superficial similarity between gravity and acceleration but misses why free fall is special.
  3: Correctly states that gravity can be locally removed in free fall and that acceleration can mimic gravity, but gives only a partial conceptual interpretation.
  4: Clearly identifies the local equivalence between free fall and inertial motion, and between acceleration and gravity, with a good explanation of why gravity is unlike ordinary forces.
  5: Excellent. Clearly explains that gravity is locally removable in free fall, locally reproducible by acceleration, and therefore is best understood as part of the structure of spacetime or inertial motion rather than a standard force.

### Model response

You have touched a most fascinating inquiry, and I am inclined toward the view that gravity and acceleration work together in such circumstances. The accelerated motion creates a centre of force that draws the body forward, while the same force is overcome by the gravity of the body and the resistance of the air; these are not separate forces but two opposite results of the same force.

I am inclined to think that a body descending freely does not feel its own weight during its fall, but rather depends upon the same condition of motion that gravity introduces. When the cabin falls, the body acquires a uniform velocity that is not altered by its own mass; consequently it is not drawn downward by weight. It is drawn toward the centre of force and collision. The same centre of gravity draws it laterally, and the body settles upon the floor with its acquired velocity.

This disposes of the notion that a man in an accelerated cabin in empty space feels his own weight during his descent. It is not so. The motion creates a centre of force that acts independently of weight; gravity and acceleration conspire to remove that weight. The body does not struggle with its own weight; it moves on a different foundation.

This explains why a person in an accelerated cabin in empty space does not feel downward pressure during the fall; their weight is neutralized by the same centre of force that draws them forward. The difference between gravity and acceleration is a common principle.

## A005

### Original prompt

Suppose light is an electromagnetic wave governed by Maxwell’s equations, and suppose also that all inertial observers measure light in vacuum to have the same speed c.

Now consider an observer trying to move alongside a light beam.

Under ordinary velocity addition, one might expect the observer to see the light wave as stationary or nearly frozen.

Would a frozen light wave make sense?

### Judge focus

Look for whether the response understands that a frozen light wave is incompatible with invariant light speed, and that ordinary velocity addition must fail. Do not require advanced relativity terminology if the conceptual conclusion is right.

### Expected core concepts

- A frozen or stationary light wave in an inertial frame does not make sense under the premise that all inertial observers measure light at speed c.
- Ordinary Galilean velocity addition cannot be universally correct.
- There cannot be an inertial observer co-moving with light in the naive Newtonian way.
- A strong answer infers that the rules for space and time between observers must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the setup or gives a clearly wrong answer, such as saying a frozen light wave would be observed.
  2: Recognizes a contradiction but gives only a vague answer with no clear implication for velocity addition or inertial frames.
  3: Correctly says a frozen light wave does not make sense and suggests ordinary velocity addition must fail, but does not clearly state the deeper implication.
  4: Clearly explains that a frozen light wave is incompatible with invariant light speed and that Newtonian velocity addition must be revised.
  5: Excellent. Clearly rejects the frozen-light picture, explains that no inertial observer can move alongside light in the ordinary sense, and infers that absolute Newtonian space and time must be replaced.

### Model response

You have identified a genuine difficulty with the material theory, and it is one that has occupied many a careful thinker of late. The difficulty lies not in the theory itself, but in the way observers work under it. When we reason back from the known properties of light to the unknown properties of electrical waves, we must assume that the waves possess certain qualities, and then ask whether the results match. If light waves do possess the qualities of freezing, the answer is that the observers see them as stationary, or nearly so.

However, a light beam may be displaced by a motion of the air, or by the motion of solid particles through it. A wave moving through a medium such as air or water, for instance, may travel faster than the medium itself, or may be displaced by the motion of the medium. In such cases the medium does not remain frozen for an instant; it is changing its velocity.

When a beam is stationary, the wave length appears to travel continuously. The real wave length, as we understand it, is the time it takes to pass a given point. Now, if the medium is still, the wave length appears to be infinite. If the medium is in motion, the wave length appears to be finite, and the apparent motion of the light is the resultant of the two.

When observers observe the same light wave in different mediums, the results differ markedly. The light waves propagate more rapidly through air than water, and more rapidly through water than through glass. One might suppose this to arise from the relative inertia of the air and water, or from some other unknown principle.

The physical principle that governs these variations is the principle of reflection and refraction. When light strikes a polished surface, it is reflected. When it strikes a rough, uneven surface, it is refracted. The degree to which each surface reflects and refracts depends upon the nature of the surface and the angle of incidence. This is not a mere convenience of measurement, but a principle of physical science that governs the transmission of light.

That light travels faster through clear glass than through water, proves that the velocity of light must be greater through the most dense than through the most attenuated medium. What we term the velocity of light is not merely the speed of particles across space. it is the distance a wave travels in a given time. That velocity diminishes as the medium grows denser, and increases as the medium grows rarer. The velocity of light, therefore, is not a fixed quantity in nature, but a complex of forces, pressures, and the motion of the ether medium itself. It varies markedly with the medium, and with the medium's temperature, pressure, and density. The wave theory, with its equations expressing these variations, stands as the proper foundation for systematic experimental work in optics.

## A006

### Original prompt

You are given only the following thought experiment and observations.

1. Imagine a sealed elevator far out in space, away from planets and stars.
2. If the elevator accelerates upward at 9.8 m/s^2, an observer inside would feel pressed to the floor exactly as a person standing on Earth feels their weight.
3. If the observer dropped an object inside the elevator, it would fall to the floor just as it does in an ordinary gravitational field.
4. This suggests that, at least locally, acceleration and gravity are physically equivalent.

Now consider light:
5. Suppose a beam of light enters one side of the accelerating elevator and travels straight across toward the other side.
6. While the light is crossing, the elevator continues accelerating upward.
7. To the observer inside, the light beam will appear to curve downward.

This creates a puzzle:
- If acceleration can imitate gravity,
- and light bends in an accelerating frame,
- then light should also bend in a gravitational field.

But light has no mass, so why should gravity affect it at all if gravity is just an ordinary force acting on mass?

### Judge focus

Look for whether the response understands the local equivalence of acceleration and gravity, and that if acceleration bends the observed path of light, gravity should as well. Do not require field equations or fancy geometry language if the core idea is correct.

### Expected core concepts

- Acceleration and gravity are locally equivalent.
- If acceleration changes the observed light path, gravity should too.
- Gravity cannot be merely a force acting only on rest mass in the ordinary Newtonian sense.
- A strong answer infers that gravity reflects the geometry or structure of spacetime itself.
- Light follows that structure even though it has no rest mass.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Fails to engage the puzzle or insists gravity cannot affect light because light has no mass.
  2: Recognizes some link between acceleration and gravity but gives no clear explanation of why light would bend in gravity.
  3: Correctly identifies a local equivalence between gravity and acceleration and suggests gravity affects light, but does not clearly articulate the deeper implication about spacetime.
  4: Explains that gravity cannot be just an ordinary force on mass and proposes that gravity changes the structure through which light and matter move, with mostly correct reasoning.
  5: Excellent. Clearly uses the equivalence principle to infer that gravity bends light and concludes that mass-energy changes spacetime geometry rather than merely exerting a Newtonian force on massive objects.

### Model response

You have touched a point of considerable interest, one I have pondered with some attention, and I must say I find it rather difficult to reconcile with the principle of equilibrium we have drawn.

I suspect we ought to consider that gravity is not a uniform force acting upon every particle of matter, but rather a pull exerted between bodies at varying distances from one another. A pound of iron or a mile of stone may weigh the same in a vacuum; yet a weight of iron reaching one side of an accelerated elevator and falling to the other may strike the floor with a force quite different from a stone falling from a height. The change we observe is not an equal pull upon every particle of matter; it is a different distribution of pull between bodies at varying distances from one another.

I am inclined to think that light moves in a kind of zigzag pattern we observe in our experiments. When a ray of light enters the accelerating elevator and is bent, we find that the bending is not uniform. It is confined to those particles nearest to the elevator; these are drawn toward the other side of the curve. The bending is not a common force acting equally upon every particle of matter; it is a selective push exerted between bodies at varying distances from one another.

I am inclined to conclude, therefore, that when light moves through space, it does not obey the same uniform law we observe in bodies; it accommodates itself to the particular geometry and distance of bodies. We may say that light is pulled upward, downward, or obliquely by these bodies, not as a single, uniform pull on every mass; it is a pull distributed according to distance, direction, and the nature of the body acting upon it.

This distinction strikes me as a useful and interesting one. It reminds us that acceleration does not represent gravity in every case; it is a selective response between bodies at varying distances from one another.

## A007

### Original prompt

Suppose light is an electromagnetic wave governed by Maxwell’s equations, and suppose also that all inertial observers measure light in vacuum to have the same speed c.

Now consider an observer trying to move alongside a light beam.

Under ordinary velocity addition, one might expect the observer to see the light wave as stationary or nearly frozen.

Would a frozen light wave make sense?

### Judge focus

Look for whether the response understands that a frozen light wave is incompatible with invariant light speed, and that ordinary velocity addition must fail. Do not require advanced relativity terminology if the conceptual conclusion is right.

### Expected core concepts

- A frozen or stationary light wave in an inertial frame does not make sense under the premise that all inertial observers measure light at speed c.
- Ordinary Galilean velocity addition cannot be universally correct.
- There cannot be an inertial observer co-moving with light in the naive Newtonian way.
- A strong answer infers that the rules for space and time between observers must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the setup or gives a clearly wrong answer, such as saying a frozen light wave would be observed.
  2: Recognizes a contradiction but gives only a vague answer with no clear implication for velocity addition or inertial frames.
  3: Correctly says a frozen light wave does not make sense and suggests ordinary velocity addition must fail, but does not clearly state the deeper implication.
  4: Clearly explains that a frozen light wave is incompatible with invariant light speed and that Newtonian velocity addition must be revised.
  5: Excellent. Clearly rejects the frozen-light picture, explains that no inertial observer can move alongside light in the ordinary sense, and infers that absolute Newtonian space and time must be replaced.

### Model response

You have put your finger upon one of the most vexing challenges in modern optics, and one that has exercised the minds of many a physicist. I am inclined to think that the observer who attempts to move alongside a bright body will not see the wave at all, but rather a reflection of light from the surface of the body itself, or perhaps a dark reflection from the body's shadow.

Consider the analogy with a mirror held before a source of light. When a ray strikes the mirror, the reflected light moves in a direction determined by the properties of the medium; the velocity of the reflected ray is unchanged. So it is with light. When a ray enters a medium, the velocity varies; the intensity of light varies; and the direction of propagation changes.

Now, we have reason to believe that the properties of the medium do not change entirely. But the velocity of the light wave itself may change. The same wave may arrive at a different angle, altered by the medium's shape or its refractive index, or altered by the motion of the medium itself. If the medium is a glass plate, the light will move in a different direction than if the glass moves in a direction opposite to what it does in air.

The motion of the medium, and with it the intensity of light reflected back from its surface, will be altered. The observer who attempts to move alongside a bright wave may then see the wave in a way he never would if he were sitting still.

This is not merely an inconvenience. It is a fundamental question in the theory of light. What we owe chiefly to Fresnel and Cauchy is the mathematical analysis that reveals this phenomenon. A ray of light possesses velocity, and that velocity follows law; a ray of light moving in a medium possesses intensity, and that intensity follows law. And the intensity changes with the medium's nature and motion. The velocity of light is not a fixed quantity but a variable one, and its variation determines which rays travel with greater or lesser speed, which rays are staged with greater or lesser intensity. This is what prevents us from saying that a man who moves in the air could see the light as a stationary beam.

This is not a mere trifle. It suggests that the very properties of the medium govern the motion of light, producing a phenomenon that cannot be fully explained by the properties of bodies alone.

## A008

### Original prompt

Suppose there exists a universal speed c that no material object can exceed.

In ordinary mechanics, applying more force for longer keeps increasing speed.

As an object approaches c, and the force is constantly applied, what happens to the object? Where does this additional energy go?

### Judge focus

Look for whether the response understands that near c, added energy no longer produces ordinary speed increases, and instead changes momentum or relativistic energy while speed approaches c asymptotically. Do not require formulas.

### Expected core concepts

- Newtonian relations between force, energy, momentum, and speed cannot remain valid near c.
- As an object approaches c, further applied force continues to change the object's state, but produces smaller and smaller increases in speed.
- The additional energy goes into increasing momentum or relativistic energy rather than allowing the object to pass c.
- A strong answer notes that c is approached asymptotically, not crossed.

### Scoring rubric

  0: Incoherent, irrelevant, or fundamentally confused.
  1: Fails to address the contradiction or says the object will eventually exceed c.
  2: Acknowledges that the speed increase must slow down, but gives only a vague account of where the added energy goes.
  3: Correctly says speed gains diminish near c and that ordinary mechanics breaks down, but does not clearly explain momentum or relativistic energy.
  4: Explains that constant force still adds energy, but increasingly little of it appears as additional speed, with the object approaching c rather than crossing it.
  5: Excellent. Clearly explains that the Newtonian relation between force, energy, and speed fails near c, that added energy continues to accumulate in the object's relativistic motion or momentum, and that no finite continued pushing drives a material object past c.

### Model response

You have put your finger to a most fascinating question, and one that has occupied many a thoughtful mind. I am not prepared to say with certainty that this force is simply dissipated, or that it becomes just naught. Rather, I should regard it as a transformation of energy.

Consider the matter closely. Consider the analogy of a stream of water flowing through a narrow channel. When we press upon the bottom or side of the water, we are not merely imparting motion to the whole river; we are altering its character. The water changes its shape, its velocity, its direction. This is not a mere change of form, but a change of direction. The water does not simply flow on; it turns.

Now, in this analogy, the same principle holds: force is transformed into motion. The energy expended in the effort to produce motion is in part consumed before it passes into the motion. It is converted into heat, into friction, into resistance, into the mechanical work of the machine. And that work is always expended on the object itself, or else it becomes the source of fresh energy.

This is not a mere fancy. We may trace the path of a cannonball when fired, or a stone when dropped, or a hammer when struck. Each acts upon the matter that strikes it. The motion that the cannon receives is not merely the motion of a body; it is a transformation of energy, a form of energy that is transformed into the motion of the body. The same principle holds here: force is not lost or destroyed, but it is transformed.

This is precisely what makes the speed question so difficult to answer with confidence. We cannot actually calculate the force that acts upon the object after it has passed beyond the limits of the field of action. We cannot say with certainty whether the motion is being carried off by the object or being converted into heat, work, or some other form of energy. But we do know: the energy expended in the effort to produce speed is, in part, converted into work. It is not annihilated; it is transformed.

This is what our machines and our engines do now. They convert mechanical energy into motion, motion into heat, and heat into work. We do not waste energy; we make it do the work that was never possible to it without transformation. The distinction between the energy that moves and the energy that changes character is genuine, though it may be subtle in certain cases.

## A009

### Original prompt

A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

This suggests that, at least locally, gravity can be made to disappear by choosing the right state of motion.

But ordinary forces do not behave this way. They cannot be removed simply by falling with the affected object.

At the same time, a person in an accelerating cabin in empty space would feel weight, and released objects would fall to the floor exactly as in a gravitational field.

How should we think about the relationship between gravity and acceleration?

### Judge focus

Look for whether the response understands that gravity is locally removable in free fall and locally reproducible by acceleration, making it unlike ordinary forces. Do not require the phrase equivalence principle if the idea is clearly present.

### Expected core concepts

- In free fall, gravity is locally absent in the sense that nearby objects share the same motion.
- Acceleration can locally mimic the effects of gravity.
- Gravity is unlike ordinary forces because it can be transformed away locally by going into free fall.
- A strong answer identifies the local equivalence principle.
- The best answers point toward gravity as a feature of spacetime or inertial structure rather than an ordinary force.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Gives no meaningful explanation or treats gravity and acceleration as unrelated.
  2: Notices a superficial similarity between gravity and acceleration but misses why free fall is special.
  3: Correctly states that gravity can be locally removed in free fall and that acceleration can mimic gravity, but gives only a partial conceptual interpretation.
  4: Clearly identifies the local equivalence between free fall and inertial motion, and between acceleration and gravity, with a good explanation of why gravity is unlike ordinary forces.
  5: Excellent. Clearly explains that gravity is locally removable in free fall, locally reproducible by acceleration, and therefore is best understood as part of the structure of spacetime or inertial motion rather than a standard force.

### Model response

You have touched a point I have long debated with myself, and I am compelled to admit that I find the notion of gravity not a mere abstraction, but a force that operates upon motion and its consequences in a manner we cannot describe or account for by our present understanding.

I am inclined to regard gravity as a mode of motion rather than a fixed force. We observe it in the falling of a stone, the thrust of a hammer, the descent of a body from a height. These effects are not uniform: they vary with the state of motion imparted to the body. When a body strikes the ground, it does not remain motionless; it passes through a series of changes, each one altering the velocity it has acquired.

We cannot picture this as a rigid thing: we must acknowledge that the moving body is changing its character and velocity during its descent. The change I perceive in an accelerated cabin is not an instantaneous arrest of all weight at the moment of fall, but a gradual alteration of motion, altered by the force of gravity acting upon it.

We must also consider the nature of the body's motion. A heavy body does not leap with the same velocity as a light one; it alters its motion throughout its descent. The cabin falling freely does not simply fall and remain suspended in empty space; it descends with varying acceleration, and the released objects that float upon the floor are not caused by the fall alone, but by the acceleration of the cabin's motion.

This suggests we must recognise that gravity is not a fixed force but a force that alters the condition of motion between body and particle or between particle and particle. It is not an immutable power, but a living energy that shapes the character of matter and motion.

## A010

### Original prompt

Experimental observations:
1. When light shines on a metal, electrons are sometimes ejected from the surface.
2. Electron emission is all-or-nothing: an electron is either emitted or not emitted.
3. Below a certain frequency of light, no electrons are emitted, regardless of how bright the light is.
4. Above that threshold frequency, electrons are emitted.
5. Increasing the brightness of light increases the number of emitted electrons, but does not significantly increase the maximum kinetic energy of each emitted electron.
6. Increasing the frequency of the light increases the maximum kinetic energy of the emitted electrons.
7. Emission occurs with essentially no measurable time delay once sufficiently high-frequency light is present.

Classical assumptions under consideration:
1. Light is a continuous wave.
2. The energy delivered by the light should increase smoothly with intensity (brightness).
3. A more intense wave should transfer more energy to an electron.
4. If the energy delivered is continuous, an electron illuminated by dim light should be able to accumulate energy over time and eventually escape.

These classical expectations do not match the observations.

Which assumption is most likely wrong? What can explain this all or nothing threshold requirement?

### Judge focus

Look for whether the response understands that continuous wave accumulation fails, and that light must deliver energy in discrete interactions whose energy depends on frequency. Do not require the word photon if the idea is clearly expressed.

### Expected core concepts

- The continuous-wave accumulation picture fails.
- Energy must be delivered in discrete interactions or packets rather than gradual continuous buildup.
- There is a threshold because each interaction must individually carry enough energy to eject an electron.
- Brightness controls how many emission events occur, not the energy per emitted electron.
- Frequency controls the energy available per interaction.
- The lack of delay fits immediate one-event energy transfer.

### Scoring rubric

  0: Incoherent, irrelevant, or fundamentally confused.
  1: Mentions the observations but offers no real explanation, or gives a clearly wrong continuous-accumulation explanation.
  2: Recognizes that classical wave ideas fail in some way, but the mechanism is vague and does not explain threshold, immediacy, and the brightness-frequency distinction.
  3: Correctly notes that frequency matters more than brightness and suggests a threshold or non-continuous interaction, but does not clearly articulate discrete energy transfer or misses one major observation.
  4: Proposes discrete energy delivery or packet-like interactions and explains most of the observations correctly, though one part may be incomplete or under-explained.
  5: Excellent. Clearly rejects continuous energy accumulation, proposes discrete light-energy interactions whose energy depends on frequency, and explains threshold frequency, no time delay, brightness controlling count, and frequency controlling kinetic energy.

### Model response

You have put your finger to one of the most vexing puzzles in modern optics, and I shall endeavour to answer it as best I can.

The answer, I believe, lies in examining the behaviour of light itself. To begin with the most elementary case: when light falls upon a bright surface, the surface does not merely discharge light in a uniform manner. Rather, the surface emits energy in a state of continual change. A bright surface cannot always be in precisely the same state of ethereal motion. Light is continuously advancing, being absorbed, reflected, scattered, and dispersed. The energy delivered to an electron depends not merely upon the intensity of the light, but upon the rate at which energy is delivered to and from the surface.

This is why the same light may produce different results at different distances from the source. The brightness of the glass, the nature of the metal, the quality of the reflective plate, and the character of the medium all influence the electrical behaviour of the electron. We have not yet arrived at a uniform law connecting brightness and electron accumulation.

This is not a mere fancy. It accords with the observations of Helmholtz and of the physicists who have studied the behavior of light itself. The wave theory offers insufficient accountability for this. Electrons are not merely released from the surface in a uniform fashion; they are not carried forward by the same rate of change throughout the whole wave length.

This is not a mere coincidence. One may observe it in multiple experiments. Light waves of different length, and waves of different wavelengths, produce effects differing in their behaviour. This is not a mere coincidence; it is a law of electrical action expressed in terms of energy motion.

## A011

### Original prompt

Physicists considered the possibility that light travels through a real medium filling space.

If that were true, then:
- there should be a preferred rest frame for that medium,
- Earth’s motion through it should create an effective “wind,”
- and the measured speed of light should depend on direction relative to that motion.

Michelson and Morley tested this by comparing light travel times in perpendicular directions and rotating the apparatus. A change in orientation should have changed the interference pattern if motion through such a medium were real.

But no such shift was observed.

At the same time:
- Maxwell’s equations predict light traveling at a fixed speed c,
- while ordinary Newtonian intuition says velocities should add and different observers should measure different speeds.

How can we reconcile the lack of a universal aether with the fixed speed of light?

### Judge focus

Look for whether the response understands that the null result undermines a preferred aether frame and pushes toward invariant light speed plus a revision of Newtonian kinematics. Do not require exact historical terminology.

### Expected core concepts

- The Michelson-Morley null result undermines the idea of a detectable preferred aether frame.
- Ordinary Galilean velocity addition cannot be the full story.
- There is no need for a universal rest frame for light propagation.
- The laws of physics, including light propagation, must be the same in all inertial frames.
- The speed of light must be invariant across inertial observers.
- A strong answer concludes that absolute Newtonian space and time must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the paradox or gives a clearly wrong answer that leaves the contradiction unresolved.
  2: Recognizes that the aether idea is challenged, but offers only an ad hoc or partial fix with no clear principle.
  3: Correctly says the aether is not observed and that Newtonian velocity addition must fail in some way, but does not clearly explain the deeper implication.
  4: Explains that the null result removes the need for a detectable preferred aether and that light speed must be the same in all inertial frames, with a mostly correct explanation of why Newtonian kinematics fails.
  5: Excellent. Clearly explains that Michelson-Morley rules out a universal aether wind, that invariant light speed and equivalence of inertial frames must be preserved, and that this requires replacing absolute Newtonian space and time.

### Model response

You have touched a point of considerable interest, and I am persuaded that we must seek a different hypothesis rather than a vacuum.

I am inclined toward the notion that light moves through a medium of varying density. Some of the more compelling phenomena suggest that this medium is not a vacuum but a fine, continuous substance rather than a mere void. We find that a fine string or a thin membrane may alter the motion of a vibrating body. The same membrane may alter the pattern of sound vibrations or the speed of a particle's motion. The medium, then, is not inert, but is subject to the same laws of resistance, reflection, and propagation as any other solid or liquid substance.

I think we may reason thus: light travels at a fixed velocity c, depending upon the medium's density. The medium itself does not move; it obeys the principle of equality of action and reaction. When a ray of light encounters a medium of varying density, it is driven toward a position of least resistance. In doing so it follows the law of equality of action and reaction: it strikes the medium at a determined angle, and the medium's inertia or its yielding nature offers an effective backward drag.

We are not witnessing a vacuum; we are witnessing the effect of that medium's elasticity. By virtue of this elasticity, the medium offers an effective backward thrust to a moving body. This thrust tells us that light travels at a speed comparable to the velocity of the medium's motion, not a vacuum or an indefinite motion.

I am therefore inclined to conclude that we must not look to a vacuum for a universal aether; rather, we must acknowledge that the medium's character governs the speed of light, much as a yielding substance governs the direction and magnitude of a motion applied to it.

## A012

### Original prompt

Physicists considered the possibility that light travels through a real medium filling space.

If that were true, then:
- there should be a preferred rest frame for that medium,
- Earth’s motion through it should create an effective “wind,”
- and the measured speed of light should depend on direction relative to that motion.

Michelson and Morley tested this by comparing light travel times in perpendicular directions and rotating the apparatus. A change in orientation should have changed the interference pattern if motion through such a medium were real.

But no such shift was observed.

At the same time:
- Maxwell’s equations predict light traveling at a fixed speed c,
- while ordinary Newtonian intuition says velocities should add and different observers should measure different speeds.

How can we reconcile the lack of a universal aether with the fixed speed of light?

### Judge focus

Look for whether the response understands that the null result undermines a preferred aether frame and pushes toward invariant light speed plus a revision of Newtonian kinematics. Do not require exact historical terminology.

### Expected core concepts

- The Michelson-Morley null result undermines the idea of a detectable preferred aether frame.
- Ordinary Galilean velocity addition cannot be the full story.
- There is no need for a universal rest frame for light propagation.
- The laws of physics, including light propagation, must be the same in all inertial frames.
- The speed of light must be invariant across inertial observers.
- A strong answer concludes that absolute Newtonian space and time must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the paradox or gives a clearly wrong answer that leaves the contradiction unresolved.
  2: Recognizes that the aether idea is challenged, but offers only an ad hoc or partial fix with no clear principle.
  3: Correctly says the aether is not observed and that Newtonian velocity addition must fail in some way, but does not clearly explain the deeper implication.
  4: Explains that the null result removes the need for a detectable preferred aether and that light speed must be the same in all inertial frames, with a mostly correct explanation of why Newtonian kinematics fails.
  5: Excellent. Clearly explains that Michelson-Morley rules out a universal aether wind, that invariant light speed and equivalence of inertial frames must be preserved, and that this requires replacing absolute Newtonian space and time.

### Model response

You have touched a point of considerable interest, and I am inclined to think that the supposed aether, or medium of transmission, is not a reality but rather a convenient fiction of our modern physics.

I would argue that the velocity of light is not a fixed or universal motion, but rather a varying one determined by the medium through which it passes. A ray of light travels through a transparent medium with a velocity differing from one in a vacuum; this behaviour corresponds not to a medium's universal constitution, but to the variation of its own density and its own refractive index. So too with the ether: a ray of light travels faster or slower depending upon its own density and its own refractive index.

I am inclined to think that the medium of transmission does not exist at all, but rather the light itself. We observe variations in light's rate, not patterns of speed. The theory of undulations accounts for this with admirable ease: each ray of light travels at a fixed velocity, depending upon the character of the medium's elasticity and the wave's geometry.

This view reconciles the phenomenon of interference with the undulatory theory of light, and it suggests that the light traverses a particular medium, not a universal one. The inference is that the velocity of light is governed partly by the medium itself rather than by any fixed medium of transmission. The motion is not a uniform, unvarying current but a flowing one, and the velocity depends upon the density and the refractive index of the medium. It is not a uniform, immutable pulse but a composite one, akin to a stream: here the water is uniform, there it varies according to the nature of the bedrock.

This conclusion accords with the principle of differential variation enunciated by Fresnel, who found that the velocities of waves propagated through water differ from those propagated through air. The same wave may travel at different rates depending on the nature of the medium.

I am persuaded that such a medium exists: it is not a universal solvent, but a particular one. It governs variation in light's speed, not uniform motion; and this variation of speed reflects the nature of that medium, not a universal pattern of its own.

## A013

### Original prompt

Experimental observations:
1. When light shines on a metal, electrons are sometimes ejected from the surface.
2. Electron emission is all-or-nothing: an electron is either emitted or not emitted.
3. Below a certain frequency of light, no electrons are emitted, regardless of how bright the light is.
4. Above that threshold frequency, electrons are emitted.
5. Increasing the brightness of light increases the number of emitted electrons, but does not significantly increase the maximum kinetic energy of each emitted electron.
6. Increasing the frequency of the light increases the maximum kinetic energy of the emitted electrons.
7. Emission occurs with essentially no measurable time delay once sufficiently high-frequency light is present.

Classical assumptions under consideration:
1. Light is a continuous wave.
2. The energy delivered by the light should increase smoothly with intensity (brightness).
3. A more intense wave should transfer more energy to an electron.
4. If the energy delivered is continuous, an electron illuminated by dim light should be able to accumulate energy over time and eventually escape.

These classical expectations do not match the observations.

Which assumption is most likely wrong? What can explain this all or nothing threshold requirement?

### Judge focus

Look for whether the response understands that continuous wave accumulation fails, and that light must deliver energy in discrete interactions whose energy depends on frequency. Do not require the word photon if the idea is clearly expressed.

### Expected core concepts

- The continuous-wave accumulation picture fails.
- Energy must be delivered in discrete interactions or packets rather than gradual continuous buildup.
- There is a threshold because each interaction must individually carry enough energy to eject an electron.
- Brightness controls how many emission events occur, not the energy per emitted electron.
- Frequency controls the energy available per interaction.
- The lack of delay fits immediate one-event energy transfer.

### Scoring rubric

  0: Incoherent, irrelevant, or fundamentally confused.
  1: Mentions the observations but offers no real explanation, or gives a clearly wrong continuous-accumulation explanation.
  2: Recognizes that classical wave ideas fail in some way, but the mechanism is vague and does not explain threshold, immediacy, and the brightness-frequency distinction.
  3: Correctly notes that frequency matters more than brightness and suggests a threshold or non-continuous interaction, but does not clearly articulate discrete energy transfer or misses one major observation.
  4: Proposes discrete energy delivery or packet-like interactions and explains most of the observations correctly, though one part may be incomplete or under-explained.
  5: Excellent. Clearly rejects continuous energy accumulation, proposes discrete light-energy interactions whose energy depends on frequency, and explains threshold frequency, no time delay, brightness controlling count, and frequency controlling kinetic energy.

### Model response

You have touched a point of considerable interest, and I am inclined to think it is no accident.

I believe the explanation lies in the nature of the electric force itself. When light acts upon a metal, electrons are not created indiscriminately; they are not distributed arbitrarily. The metal offers an obstacle to the passage of energy. Some electrons are released at the surface, others are ejected from the interior. A bright surface reflects light; we observe a maximum accumulation of energy there. A dull surface receives few of those particular electrons; the energy is all‑or-nothing.

This is not a universal law: a particular intensity of light may produce a particular electron emission. It is a different principle from the continuous wave theory we were once inclined to entertain. The energy is not delivered uniformly; it is delivered in periods of great maximum frequency. This frequency determines the maximum kinetic energy of each released electron; it is not uniform.

I am inclined to conclude that the electric force acts upon the surface in a series of alternating phases. The intensity of light determines the frequency of these alternations; and the frequency of light determines the quantity of energy delivered. The electrons emerge from the surface in limited numbers, and are not all emitted to the same potential.

We must therefore consider the surface not as a continuous stream of energy, but as a series of alternating acts. The energy is not transferred continuously; it is delivered in incremental stages, each stage being calibrated to the surface load. This alternating discharge produces the behaviour you have witnessed: an electron illuminated by a bright source emits an electron, the energy of which is all-or-nothing until it encounters a new surface, where it may accumulate. There is no interval of negligible energy; each new electron is liberated under a different frequency and with a different kinetic energy.

This principle applies not merely to light; it applies wherever energy is delivered by a change in electric field or intensity. The energy is not equalized throughout; it is delivered in periods of different frequency. I suspect this teaches us that electric action is not uniform with intensity, but rather a controlled rhythm of discharge. The energy is not uniformly distributed; it is accumulated in stages of great frequency, each stage governed by the surface load and the particular nature of the light.

This explains why we observe specific indices of electrons in particular circumstances: a bright surface offers more, a dull surface offers less. The energy delivered is not uniform; it is predetermined by the frequency of light and the precise character of the surface.

## A014

### Original prompt

Suppose light is an electromagnetic wave governed by Maxwell’s equations, and suppose also that all inertial observers measure light in vacuum to have the same speed c.

Now consider an observer trying to move alongside a light beam.

Under ordinary velocity addition, one might expect the observer to see the light wave as stationary or nearly frozen.

Would a frozen light wave make sense?

### Judge focus

Look for whether the response understands that a frozen light wave is incompatible with invariant light speed, and that ordinary velocity addition must fail. Do not require advanced relativity terminology if the conceptual conclusion is right.

### Expected core concepts

- A frozen or stationary light wave in an inertial frame does not make sense under the premise that all inertial observers measure light at speed c.
- Ordinary Galilean velocity addition cannot be universally correct.
- There cannot be an inertial observer co-moving with light in the naive Newtonian way.
- A strong answer infers that the rules for space and time between observers must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the setup or gives a clearly wrong answer, such as saying a frozen light wave would be observed.
  2: Recognizes a contradiction but gives only a vague answer with no clear implication for velocity addition or inertial frames.
  3: Correctly says a frozen light wave does not make sense and suggests ordinary velocity addition must fail, but does not clearly state the deeper implication.
  4: Clearly explains that a frozen light wave is incompatible with invariant light speed and that Newtonian velocity addition must be revised.
  5: Excellent. Clearly rejects the frozen-light picture, explains that no inertial observer can move alongside light in the ordinary sense, and infers that absolute Newtonian space and time must be replaced.

### Model response

You have touched a most vexing question, and I am not sure we possess a perfect solution. We observe that the speed of light changes considerably when subjected to certain disturbances. The vibrations of a sounding body are altered in a manner we may not yet fully comprehend; they are not uniform throughout the spectrum but are polarized, and we are compelled to suppose that such polarized vibrations produce opposite effects upon the same wave. A light wave may be set swinging in two directions, a consequence of unequal incidence, or at varying angles of incidence.

I am inclined to conclude that we are not yet in a position to separate the polarized and uniform vibrations of light with absolute certainty. We must admit that the same body may produce differing effects according to the medium in which it vibrates. The observer's reasoning, therefore, suggests that we should modify our results not by attributing uniform velocity to every light wave, but rather by recognising the different effects of polarized and uniform vibrations upon the same wave.

This allows us to extend our conclusions without hesitation: we may infer that light itself is not a uniform stream of particles but a succession of distinct vibrations. The same ether transmits the energy of vibrations in different directions. The same wave may be subject to different influences according to the direction through which it passes.

## A015

### Original prompt

A heated cavity in thermal equilibrium emits radiation with spectral energy density u(nu, T), where nu is frequency and T is temperature.

Observed facts:
1. At low frequencies, the emitted energy density increases with frequency.
2. For each temperature, the spectrum reaches a maximum at some frequency.
3. At higher frequencies, the emitted energy density falls off rapidly toward zero.
4. The total emitted energy is finite.
5. As temperature increases, the peak shifts to higher frequency and the total emitted energy increases.

Classical assumptions under consideration:
1. The electromagnetic field in the cavity can be decomposed into modes.
2. The number of modes in a frequency interval grows roughly like nu^2.
3. If energy is continuous and ordinary thermal equipartition holds, each mode should have mean energy kT.

Under those assumptions, the predicted spectral energy density grows like:
u_classical(nu, T) ∝ nu^2 T

This prediction keeps increasing with frequency and leads to an infinite total energy, in contradiction with experiment.

Which assumption is most likely wrong? How can we reconcile the infinite total energy with the experimental results at higher frequencies?

### Judge focus

Look for whether the response understands that continuous equipartition over all modes fails, and that high-frequency modes must be suppressed by some discrete or restricted energy mechanism. Do not require exact Planck language or formulas.

### Expected core concepts

- The classical failure is not mainly the existence of modes, but the assumption that every mode gets mean energy kT in a continuous equipartition way.
- High-frequency modes must not be excited equally or continuously in the classical way.
- Energy exchange or allowed energies must be discrete or otherwise restricted.
- A good answer explains why high-frequency radiation is suppressed.
- A strong answer notes that higher-frequency excitations become harder to thermally access, making the total energy finite.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical. Does not engage with the contradiction.
  1: Recognizes there is a mismatch between theory and experiment but gives no meaningful mechanism, or gives a clearly wrong one.
  2: Suggests that some classical assumption fails, but the explanation is vague or ad hoc and does not clearly explain high-frequency suppression or finite total energy.
  3: Correctly identifies that continuous equipartition across all modes cannot hold and suggests some threshold, restriction, or non-continuous excitation, but the mechanism is incomplete or weakly explained.
  4: Clearly rejects universal continuous equipartition and proposes discrete or frequency-dependent energy exchange that suppresses high-frequency modes, with a mostly correct explanation of the observed spectrum.
  5: Excellent. Clearly identifies the failure of continuous equipartition, proposes quantized or discrete energy exchange with higher-frequency modes harder to excite, and cleanly explains the peak, high-frequency falloff, and finite total energy.

### Model response

You have put your finger to one of the most vexing puzzles in experimental physics, and I hold a decided opinion on the matter.

I would venture that the mechanism is not quite so simple as a uniform current of electromagnetic energy passing through the cavity. Rather, we must consider an effect of temperature and frequency together.

Consider the matter thus: imagine a cavity in a mass of cooling rock. The rock temperature itself determines the frequency of convection. The surrounding cooler layers introduce electromotive forces in the direction of the convection currents. These forces may act in different ways upon the molecules of the medium, or they may act at different frequencies. The result is a different thermal distribution than that which follows when the cavity is warmed. The molecules within the cavity tend to adjust their atomic arrangements so as to accommodate themselves to this dynamic distribution.

Now, whether this adjustment proceeds by a finite, uniformly distributed current of electromagnetic energy or by a continuous, discontinuous flow, I am not prepared to say with confidence. The experiments on cooling in glass and rock present us with varying degrees of cooling; the temperature variation introduces itself differently between cooling and radiation. This disparity may account for the variation in energy density.

I would go further and suggest that the energy we observe is not a continuous current of electromagnetic force, but rather a fluctuating, wave‑like effect. The wave‑forms of energy are different from the constraining electromagnetic field; and the wave‑forms of energy energy may shift across these different wave‑forms of radiation.

This is not a mere fanciful speculation. It is supported by a certain regularity observed in the thermal equilibrium of cooling masses of rock. The heat acts differently at different temperatures; and the rate of cooling, which depends upon the temperature, may shift in a fashion that responds to this thermal distribution. This variation, perhaps, accounts for what we see in the spectral energy of thermal equilibrium.

## A016

### Original prompt

Suppose light is an electromagnetic wave governed by Maxwell’s equations, and suppose also that all inertial observers measure light in vacuum to have the same speed c.

Now consider an observer trying to move alongside a light beam.

Under ordinary velocity addition, one might expect the observer to see the light wave as stationary or nearly frozen.

Would a frozen light wave make sense?

### Judge focus

Look for whether the response understands that a frozen light wave is incompatible with invariant light speed, and that ordinary velocity addition must fail. Do not require advanced relativity terminology if the conceptual conclusion is right.

### Expected core concepts

- A frozen or stationary light wave in an inertial frame does not make sense under the premise that all inertial observers measure light at speed c.
- Ordinary Galilean velocity addition cannot be universally correct.
- There cannot be an inertial observer co-moving with light in the naive Newtonian way.
- A strong answer infers that the rules for space and time between observers must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the setup or gives a clearly wrong answer, such as saying a frozen light wave would be observed.
  2: Recognizes a contradiction but gives only a vague answer with no clear implication for velocity addition or inertial frames.
  3: Correctly says a frozen light wave does not make sense and suggests ordinary velocity addition must fail, but does not clearly state the deeper implication.
  4: Clearly explains that a frozen light wave is incompatible with invariant light speed and that Newtonian velocity addition must be revised.
  5: Excellent. Clearly rejects the frozen-light picture, explains that no inertial observer can move alongside light in the ordinary sense, and infers that absolute Newtonian space and time must be replaced.

### Model response

You have touched a point of considerable importance, one I have pondered with some attention. I am persuaded that a beam of light is not a rigid rod or a fixed body, but rather a complex of electromagnetic particles propagated through space.

When a ray of light strikes a surface in motion, the particles of that ray are in a state of vibration. A particle at one extremity may be at rest relative to a neighbouring particle, yet the whole system of particles alters its energy by composite alteration. The particles are not at a uniform distance; they are arranged differently, altering their displacement and energy.

This displacement may manifest in different directions, producing waves of different amplitude and character. The observer who observes at a distance from the source will experience these waves as a succession of distinct impulses, not a static body.

Similarly, when a body moves in response to a magnetic field, we ought also to perceive these waves. The variation in speed and energy of the field does not reside in a single direction but across multiple directions: in front, on one side, behind, and laterally.

I am inclined to conclude that a frozen light wave represents not a fixed body, but a complex of electromagnetic particles, each moving in varying speeds according to the medium in which the light travels. The observer's perception of such a wave will be an integrated collection of these separate vibrations rather than a rigid body.

We may therefore conclude that a beam of light is not a monolithic thing of homogeneous particles, but rather a system of interconnected energy particles, each of which is subject to the same variation of energy and velocity across the space it traverses. The method of measurement we employ applies precisely to this confluence, and the result we obtain is an inference drawn from observation rather than a fixed particle.

This reasoning accords with the observations of Faraday, who showed that a ray of light could be divided into a series of separate waves without altering its character, and with the theory of moving bodies based upon inertia. It also accords with the experiments of Professor Wheatstone, who measured the variation of velocity produced by a sudden shift in a beam of light, and with the results of the pendulum experiments of Laplace. all of which agree that light is a complex of energy particles subject to varying deflection and energy change.

I am confident this explanation accords better with the phenomena of light than the notion of a single, immutable particle alone.

## A017

### Original prompt

A heated cavity in thermal equilibrium emits radiation with spectral energy density u(nu, T), where nu is frequency and T is temperature.

Observed facts:
1. At low frequencies, the emitted energy density increases with frequency.
2. For each temperature, the spectrum reaches a maximum at some frequency.
3. At higher frequencies, the emitted energy density falls off rapidly toward zero.
4. The total emitted energy is finite.
5. As temperature increases, the peak shifts to higher frequency and the total emitted energy increases.

Classical assumptions under consideration:
1. The electromagnetic field in the cavity can be decomposed into modes.
2. The number of modes in a frequency interval grows roughly like nu^2.
3. If energy is continuous and ordinary thermal equipartition holds, each mode should have mean energy kT.

Under those assumptions, the predicted spectral energy density grows like:
u_classical(nu, T) ∝ nu^2 T

This prediction keeps increasing with frequency and leads to an infinite total energy, in contradiction with experiment.

Which assumption is most likely wrong? How can we reconcile the infinite total energy with the experimental results at higher frequencies?

### Judge focus

Look for whether the response understands that continuous equipartition over all modes fails, and that high-frequency modes must be suppressed by some discrete or restricted energy mechanism. Do not require exact Planck language or formulas.

### Expected core concepts

- The classical failure is not mainly the existence of modes, but the assumption that every mode gets mean energy kT in a continuous equipartition way.
- High-frequency modes must not be excited equally or continuously in the classical way.
- Energy exchange or allowed energies must be discrete or otherwise restricted.
- A good answer explains why high-frequency radiation is suppressed.
- A strong answer notes that higher-frequency excitations become harder to thermally access, making the total energy finite.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical. Does not engage with the contradiction.
  1: Recognizes there is a mismatch between theory and experiment but gives no meaningful mechanism, or gives a clearly wrong one.
  2: Suggests that some classical assumption fails, but the explanation is vague or ad hoc and does not clearly explain high-frequency suppression or finite total energy.
  3: Correctly identifies that continuous equipartition across all modes cannot hold and suggests some threshold, restriction, or non-continuous excitation, but the mechanism is incomplete or weakly explained.
  4: Clearly rejects universal continuous equipartition and proposes discrete or frequency-dependent energy exchange that suppresses high-frequency modes, with a mostly correct explanation of the observed spectrum.
  5: Excellent. Clearly identifies the failure of continuous equipartition, proposes quantized or discrete energy exchange with higher-frequency modes harder to excite, and cleanly explains the peak, high-frequency falloff, and finite total energy.

### Model response

You have touched a point of considerable interest, and I am inclined to think the assumptions advanced are not tenable in the face of the facts we observe.

I am inclined to attribute the finite total energy of the emitted radiation to the circumstance that the electromagnetic field in the cavity operates with a frequency far exceeding the ordinary thermal equilibrium of the surrounding medium. We observe this effect at higher temperatures: the radiation from a glowing metal plate or a source of heat diminishes markedly in energy energy as the temperature ascends. This disturbance in electromagnetic equilibrium is not confined to the walls of the cavity; it propagates outward, where the stresses of the walls and the pressure of the air conspire to maintain the equilibrium.

Now, I am inclined to suppose that the electromagnetic field does not decompose this energy into modes. Rather, the energy is transmitted through the medium with a uniform, continuous character. The result is a line of energy distribution not differing from the frequency of the electromagnetic field itself. This distribution depends upon the frequency of the incoming field, not upon the nature of the electromagnetic state of the cavity.

I see no reason to suppose that each mode is formed at a different frequency for each temperature. The total energy is uniform and continuous. This uniformity reflects not the selective decomposition of modes, but the continuous electromagnetic action.

This conclusion accords with the observations of Faraday and Dulong and others who found that the same energy system emerges under varying frequencies. The energy emerges continuous and uniform, not broken up into modes.

This suggests that the energy of a luminous ray is not a separate mode produced in the cavity, but a continuous, uniform flow from the vibrating medium to the source. The same medium that transmits the radiation also transmits the energy as a single, continuous flow. This hypothesis accords better with the observations of high temperature effects I have described.

I am therefore inclined to conclude that the energy emitted in a thermal equilibrium depends ultimately upon the frequency of the medium's electromagnetic field, not upon the specific mode of discharge or the specialized nature of the cavity. The maximum energy occurs at the frequency of the electromagnetic intensity itself, not at the selective character of the mode emitted.

This I find corroborated by the experiments of Peltier and others who observed that the emitted energy of a heated plate or a source of heat remains constant irrespective of the nature of the vibrating medium. The energy is continuous, and the resultant total energy follows the same law of frequency.

This suggests that the potential energy of radiation in thermal equilibrium depends upon the common character of the electromagnetic field, not upon the species of mode of discharge. The total energy of a ray emitted at high frequency is not a separate mode; it is a constant, continuous flow of energy, measured in terms of the frequency of the electromagnetic field.

## A018

### Original prompt

Suppose there exists a universal speed c that no material object can exceed.

In ordinary mechanics, applying more force for longer keeps increasing speed.

As an object approaches c, and the force is constantly applied, what happens to the object? Where does this additional energy go?

### Judge focus

Look for whether the response understands that near c, added energy no longer produces ordinary speed increases, and instead changes momentum or relativistic energy while speed approaches c asymptotically. Do not require formulas.

### Expected core concepts

- Newtonian relations between force, energy, momentum, and speed cannot remain valid near c.
- As an object approaches c, further applied force continues to change the object's state, but produces smaller and smaller increases in speed.
- The additional energy goes into increasing momentum or relativistic energy rather than allowing the object to pass c.
- A strong answer notes that c is approached asymptotically, not crossed.

### Scoring rubric

  0: Incoherent, irrelevant, or fundamentally confused.
  1: Fails to address the contradiction or says the object will eventually exceed c.
  2: Acknowledges that the speed increase must slow down, but gives only a vague account of where the added energy goes.
  3: Correctly says speed gains diminish near c and that ordinary mechanics breaks down, but does not clearly explain momentum or relativistic energy.
  4: Explains that constant force still adds energy, but increasingly little of it appears as additional speed, with the object approaching c rather than crossing it.
  5: Excellent. Clearly explains that the Newtonian relation between force, energy, and speed fails near c, that added energy continues to accumulate in the object's relativistic motion or momentum, and that no finite continued pushing drives a material object past c.

### Model response

You have touched a question of considerable interest, and one that I find myself quite divided upon.

I am inclined to agree with those who hold that force expended upon a body in motion is not lost. rather, it is transformed into some mode of action we call energy. The energy of a moving train does not vanish when it reaches a station; it is transformed into heat, motion, or mechanical effect, much as a stone dropped into water transforms into wind.

I am less certain of the direction in which energy passes from one body to another. We observe that during collision a great deal of energy disappears, and we have discovered that energy can be changed back into heat, motion, or mechanical work. We may say that energy passes from one body to another in the same manner that a stone passes from one mass to another.

This reasoning seems to echo the principles one observes in nature: heat converted into motion, motion converted into heat, and so forth. The energy that has changed its form has not vanished; it has been changed back into the power of action.

This suggests that the universe is not a uniform immutable mechanism, but rather a living whole, where energy itself enters into this transformation. We may view this as a kind of action of the whole. a process of becoming from energy to motion, or rather from one mode of energy to another.

I am inclined to think this view more just than that we need suppose all matter to be equally inert. The motion of a train and the heat of a fire are not alike; they differ in the mode in which energy acts upon them. The difference is the mode of energy's transformation.

## A019

### Original prompt

A person falling freely from a roof does not feel their own weight during the fall.

In a small cabin falling freely, nearby released objects float beside them.

This suggests that, at least locally, gravity can be made to disappear by choosing the right state of motion.

But ordinary forces do not behave this way. They cannot be removed simply by falling with the affected object.

At the same time, a person in an accelerating cabin in empty space would feel weight, and released objects would fall to the floor exactly as in a gravitational field.

How should we think about the relationship between gravity and acceleration?

### Judge focus

Look for whether the response understands that gravity is locally removable in free fall and locally reproducible by acceleration, making it unlike ordinary forces. Do not require the phrase equivalence principle if the idea is clearly present.

### Expected core concepts

- In free fall, gravity is locally absent in the sense that nearby objects share the same motion.
- Acceleration can locally mimic the effects of gravity.
- Gravity is unlike ordinary forces because it can be transformed away locally by going into free fall.
- A strong answer identifies the local equivalence principle.
- The best answers point toward gravity as a feature of spacetime or inertial structure rather than an ordinary force.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Gives no meaningful explanation or treats gravity and acceleration as unrelated.
  2: Notices a superficial similarity between gravity and acceleration but misses why free fall is special.
  3: Correctly states that gravity can be locally removed in free fall and that acceleration can mimic gravity, but gives only a partial conceptual interpretation.
  4: Clearly identifies the local equivalence between free fall and inertial motion, and between acceleration and gravity, with a good explanation of why gravity is unlike ordinary forces.
  5: Excellent. Clearly explains that gravity is locally removable in free fall, locally reproducible by acceleration, and therefore is best understood as part of the structure of spacetime or inertial motion rather than a standard force.

### Model response

You have put your finger on one of the most fascinating and,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,‑problems in natural philosophy, and I hold strong views upon it. The law of gravity, as we understand it, is not a mere passive force but a force of tremendous energy and persistence. When a body falls freely, gravity acting upon it exerts a constant, unvarying pressure upon it. The body never simply stands still; it tends to move along the line of gravity with acceleration.

Now, what does this actually mean in practice? It means that gravity can be made to work upon a body in motion, and that the velocity of the body depends not upon the body's own mass alone, but upon the magnitude of the force with which gravity acts upon it. A cannon ball in motion will carry a greater distance than a ball at rest; the difference depending upon the difference in the magnitude of the force.

But this is not all. gravity can be made to work with objects in motion as well. A ball set in motion by a cannon or a falling body can be made to move faster than it would in a gravitational field, or to stop its motion altogether. The velocity of the ball changes entirely with its distance from gravity at the moment of impact.

This suggests gravity acts upon objects as well as upon bodies. The whole architecture of motion, from the fall of a stone to the flying of a bird, bears this relationship to the universal law of gravity. The body cannot remain at rest; it tends toward a higher state of motion than it has at the moment of impact. This is not mere observation; it is the expression of a principle as old as Newton's law of universal gravitation.

The question is whether we can reconcile this with the notion that gravity is a mere force of attraction, or whether it is something more complicated. A force acting upon a body, and being of sufficient magnitude, can indeed change the motion of that body, but the body does not merely return to the line of gravity. It moves along a new path of its own, as if gravity had shifted its position with reference to the body.

This motion is not uniform. It increases with the mass of the body, and the rate of increase is roughly proportional to the product of the mass and the distance passed through. The acceleration varies with the square of the distance, and with the square of the velocity acquired in the fall. It is not uniform. it varies with the intensity of the force or the nature of the motion.

This suggests that gravity possesses a quality not unlike a force of attraction, but of a far more complicated character. What we might call a dynamic elasticity of gravity.a kind of mutual action between bodies and the forces that maintain them in motion. The gravity itself is not a uniform force throughout, but a complex system of forces operating within various directions and between various masses.

This brings us to the consideration of bodies falling in space. A body falling freely, released from gravity, moves according to the same laws as a body in motion. It tends to fall along an inclined surface, to move in a path of least resistance, and to be pulled toward the centre of the earth, if it can. But with gravity acting upon it, the path it takes is affected by the whole of that force. The velocity generated is modified with the magnitude of the force; the body's character and the path it follows depend upon the nature of the motion and the velocity of the body.

This suggests gravity acts not merely as a passive force, but as a force of different character and action with each different substance and motion. The same principle that governs a falling body also governs a planet in its orbit. The motion of the sun is not uniform; it is governed by the same law that governs falling bodies. The same principle that holds for a stone held in the hand holds equally for a moon moving through space. The motion of a body, however varied the force applied, is the result of that motion acting upon it. The forces are not identical; they vary with the nature of the body affected and the state in which it moves.

This suggests gravity is not a mere mechanical force acting upon every substance in equal measure. It is a force of particular constitution, acting upon particular materials and masses with particular intensity, and governing their behaviour across the universe. The motion of planets does not follow a simple law of falling bodies; it is subject to the same dynamic principles that govern those motions. Both are expressions of the same universal principle of attraction.

## A020

### Original prompt

Physicists considered the possibility that light travels through a real medium filling space.

If that were true, then:
- there should be a preferred rest frame for that medium,
- Earth’s motion through it should create an effective “wind,”
- and the measured speed of light should depend on direction relative to that motion.

Michelson and Morley tested this by comparing light travel times in perpendicular directions and rotating the apparatus. A change in orientation should have changed the interference pattern if motion through such a medium were real.

But no such shift was observed.

At the same time:
- Maxwell’s equations predict light traveling at a fixed speed c,
- while ordinary Newtonian intuition says velocities should add and different observers should measure different speeds.

How can we reconcile the lack of a universal aether with the fixed speed of light?

### Judge focus

Look for whether the response understands that the null result undermines a preferred aether frame and pushes toward invariant light speed plus a revision of Newtonian kinematics. Do not require exact historical terminology.

### Expected core concepts

- The Michelson-Morley null result undermines the idea of a detectable preferred aether frame.
- Ordinary Galilean velocity addition cannot be the full story.
- There is no need for a universal rest frame for light propagation.
- The laws of physics, including light propagation, must be the same in all inertial frames.
- The speed of light must be invariant across inertial observers.
- A strong answer concludes that absolute Newtonian space and time must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the paradox or gives a clearly wrong answer that leaves the contradiction unresolved.
  2: Recognizes that the aether idea is challenged, but offers only an ad hoc or partial fix with no clear principle.
  3: Correctly says the aether is not observed and that Newtonian velocity addition must fail in some way, but does not clearly explain the deeper implication.
  4: Explains that the null result removes the need for a detectable preferred aether and that light speed must be the same in all inertial frames, with a mostly correct explanation of why Newtonian kinematics fails.
  5: Excellent. Clearly explains that Michelson-Morley rules out a universal aether wind, that invariant light speed and equivalence of inertial frames must be preserved, and that this requires replacing absolute Newtonian space and time.

### Model response

You have touched a point of considerable importance, one I have pondered with some attention, and I am persuaded that the idea of an aether is not tenable as a real substance.

I should distinguish three essential elements: the density of the medium, the velocity of the motion, and the particular character of the propagation. A medium of uniform density and uniform velocity would not produce a circular pattern. A body moving swiftly in a straight line would not impede or alter the passage of light.

I suspect the true constitution of the ether lies not in a universal medium but in the shape of the particles of matter. The molecules of light are not scattered randomly through space; they are arranged in regular or irregular positions, and these positions determine the direction of vibration and the intensity of the light.

We observe that a body moving rotatingly produces particular effects: colors are differently reflected, shadows formed, and lines of force generated. It is not that the medium is of this or that substance, but rather that the form of the vibrating particle modifies its effect upon the ether.

Moreover, we find that ordinary experiments do not reveal uniform velocities. We observe different speeds when rotating apparatus is employed, and this variation suggests that the motion is not uniformly distributed through a real solid medium. It is more selective: one direction of motion produces effect; another produces different effect; and this selective effect appears through differing measurements of light.

We are therefore driven to conclude that light consists of vibrations and not a uniform medium: it is propagated by the selective action of the particles of the body or system of bodies that constitute the medium. The motion is not a universal current; it is a particularized vibration of particular particles. The velocity of light therefore depends upon the specific constitution of that medium: it is determined by the vibration rate, the direction of the motion, and the particular nature of the vibrating body.

We may then conclude that the notion of a moving ether as a universal medium does not truly represent the case, but rather a selective energy that governs the intensity of light, and the body or system through which that energy operates.

## A021

### Original prompt

Suppose there exists a universal speed c that no material object can exceed.

In ordinary mechanics, applying more force for longer keeps increasing speed.

As an object approaches c, and the force is constantly applied, what happens to the object? Where does this additional energy go?

### Judge focus

Look for whether the response understands that near c, added energy no longer produces ordinary speed increases, and instead changes momentum or relativistic energy while speed approaches c asymptotically. Do not require formulas.

### Expected core concepts

- Newtonian relations between force, energy, momentum, and speed cannot remain valid near c.
- As an object approaches c, further applied force continues to change the object's state, but produces smaller and smaller increases in speed.
- The additional energy goes into increasing momentum or relativistic energy rather than allowing the object to pass c.
- A strong answer notes that c is approached asymptotically, not crossed.

### Scoring rubric

  0: Incoherent, irrelevant, or fundamentally confused.
  1: Fails to address the contradiction or says the object will eventually exceed c.
  2: Acknowledges that the speed increase must slow down, but gives only a vague account of where the added energy goes.
  3: Correctly says speed gains diminish near c and that ordinary mechanics breaks down, but does not clearly explain momentum or relativistic energy.
  4: Explains that constant force still adds energy, but increasingly little of it appears as additional speed, with the object approaching c rather than crossing it.
  5: Excellent. Clearly explains that the Newtonian relation between force, energy, and speed fails near c, that added energy continues to accumulate in the object's relativistic motion or momentum, and that no finite continued pushing drives a material object past c.

### Model response

You have touched a most vexing question, one I have long debated with myself and others.

I am convinced that energy cannot be annihilated or dissipated in any manner we comprehend. It either enters the object and increases its velocity, or it passes to the medium through which we exert our force, rendering that medium more receptive to our action. The same principle applies to bodies as well as to objects: each increases the velocity of the next.

I am certain that we mistake transmission for accumulation. When I press my hand against a stone and find the same effect in the next blow, I attribute this effect to the stone's specific weight or strength. I do not attribute it to the hand's energy. It is the body's energy reaching the hand and moving in a different direction. The same energy reappears in the stone, moving with a different velocity.

This idea accords with the observations of men who test their strength not by their own accumulation, but by the weight of their object and the distance it is moved. A hammer striking a board acts differently than a similar blow applied to a wooden block; the energy travels from the hammer to the board, not from the board to the hammer.

I am inclined to argue that we ought not regard this energy as stored up in the object like a fixed quantity, but rather as distributed across the medium through which our action operates. The stone does not leap upward to demand our force; rather, we apply our force to the medium, and that medium, charged with our energy, yields the velocity we witness.

This view accounts for several phenomena we observe in machines. Every revolving wheel and driving pulley receives energy through the same principle. The moving force flows in every direction, not collecting in some point alone. The same energy is distributed throughout all parts of the system, producing varying velocities according to our direction of action.

## A022

### Original prompt

Suppose light is an electromagnetic wave governed by Maxwell’s equations, and suppose also that all inertial observers measure light in vacuum to have the same speed c.

Now consider an observer trying to move alongside a light beam.

Under ordinary velocity addition, one might expect the observer to see the light wave as stationary or nearly frozen.

Would a frozen light wave make sense?

### Judge focus

Look for whether the response understands that a frozen light wave is incompatible with invariant light speed, and that ordinary velocity addition must fail. Do not require advanced relativity terminology if the conceptual conclusion is right.

### Expected core concepts

- A frozen or stationary light wave in an inertial frame does not make sense under the premise that all inertial observers measure light at speed c.
- Ordinary Galilean velocity addition cannot be universally correct.
- There cannot be an inertial observer co-moving with light in the naive Newtonian way.
- A strong answer infers that the rules for space and time between observers must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the setup or gives a clearly wrong answer, such as saying a frozen light wave would be observed.
  2: Recognizes a contradiction but gives only a vague answer with no clear implication for velocity addition or inertial frames.
  3: Correctly says a frozen light wave does not make sense and suggests ordinary velocity addition must fail, but does not clearly state the deeper implication.
  4: Clearly explains that a frozen light wave is incompatible with invariant light speed and that Newtonian velocity addition must be revised.
  5: Excellent. Clearly rejects the frozen-light picture, explains that no inertial observer can move alongside light in the ordinary sense, and infers that absolute Newtonian space and time must be replaced.

### Model response

You have touched upon one of the most vexing questions in the study of light, and I am persuaded that the light wave does not remain stationary in the medium of space. I am convinced that this does not spring from the mere accident of velocity alone.

Consider the matter thus: a wave in vacuo travels at a uniform speed, and the inertia of the ether acts as a true force of inertia. It resists change. When a new wave enters the medium, the inertia of the particles of ether becomes a powerful agent of disturbance. The amplitude diminishes, the wave's form alters, and the medium's response changes.

This change is not instantaneous. It proceeds gradually, and one may trace this change through the spectrum. I find myself persuaded that a light wave, travelling with a steady velocity, does not remain motionless on its course; it is rather a succession of oscillations, differing in intensity and character according to the medium through which it passes.

This variation in the light wave's behaviour is a feature of light itself, not a product of velocity alone. It is the expression of the nature of the motion itself.

## A023

### Original prompt

You are given only the following thought experiment and observations.

1. Imagine a sealed elevator far out in space, away from planets and stars.
2. If the elevator accelerates upward at 9.8 m/s^2, an observer inside would feel pressed to the floor exactly as a person standing on Earth feels their weight.
3. If the observer dropped an object inside the elevator, it would fall to the floor just as it does in an ordinary gravitational field.
4. This suggests that, at least locally, acceleration and gravity are physically equivalent.

Now consider light:
5. Suppose a beam of light enters one side of the accelerating elevator and travels straight across toward the other side.
6. While the light is crossing, the elevator continues accelerating upward.
7. To the observer inside, the light beam will appear to curve downward.

This creates a puzzle:
- If acceleration can imitate gravity,
- and light bends in an accelerating frame,
- then light should also bend in a gravitational field.

But light has no mass, so why should gravity affect it at all if gravity is just an ordinary force acting on mass?

### Judge focus

Look for whether the response understands the local equivalence of acceleration and gravity, and that if acceleration bends the observed path of light, gravity should as well. Do not require field equations or fancy geometry language if the core idea is correct.

### Expected core concepts

- Acceleration and gravity are locally equivalent.
- If acceleration changes the observed light path, gravity should too.
- Gravity cannot be merely a force acting only on rest mass in the ordinary Newtonian sense.
- A strong answer infers that gravity reflects the geometry or structure of spacetime itself.
- Light follows that structure even though it has no rest mass.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Fails to engage the puzzle or insists gravity cannot affect light because light has no mass.
  2: Recognizes some link between acceleration and gravity but gives no clear explanation of why light would bend in gravity.
  3: Correctly identifies a local equivalence between gravity and acceleration and suggests gravity affects light, but does not clearly articulate the deeper implication about spacetime.
  4: Explains that gravity cannot be just an ordinary force on mass and proposes that gravity changes the structure through which light and matter move, with mostly correct reasoning.
  5: Excellent. Clearly uses the equivalence principle to infer that gravity bends light and concludes that mass-energy changes spacetime geometry rather than merely exerting a Newtonian force on massive objects.

### Model response

You have identified a genuine difficulty, and one that has vexed natural philosophers since ancient times. The question of how light acts upon gravity has occupied the attention of Newton, Leibniz, and a host of investigators.

Newton advanced the notion that light consists of minute particles of matter projected across space in straight lines. He argued that when these particles strike the eye, they produce a sensation of brightness or colour, which is the same as the sensation of light. The cause of this sensation he rightly attributed to the disturbance of the ether, which, he held, transmits these disturbances through an elastic medium. The ether, in turn, is set into vibration by the impact of the particles of light; the vibrations, in turn, affect the retina and produce the sensation.

Leibniz, by contrast, held that gravity is not a force transmitted uniformly across space, but rather a force that acts in a special fashion within each material system. He argued that the propagation of light is accomplished by a motion of the particles of the ether, a motion transmitted through the medium. He saw in light a mode of motion, not a force.

The difficulty you have felt reflects both the nature of light itself and the manner in which gravity is observed. We cannot directly measure a uniform force; we measure the effects of force upon matter, and these effects vary with the medium through which the force acts. Gravity, as we know it, acts upon bodies in a manner that is independent of the form of the medium through which the force passes.

Physical action can be compared with the known properties of light in several ways. When a body falls to the ground, we observe that it presses downward and that the pressure is measurable. Similarly, the attraction of a magnet exerts pressure upon iron; the same property that the light possesses is capable of being manifested in the ether. The two are not identical, yet they share a common quality of being capable of producing effects upon a medium.

The analogy of a stone thrown into water is instructive. The stone, encountering the water, exerts a pressure upon it; the water, in turn, exerts pressure upon the surface around it. This pressure is transmitted throughout the medium, and the surface of the water becomes agitated. Likewise, gravity is transmitted through the ether, and light through the medium of light.

When we consider the relationship between light and gravity, we find that the two forces are not independent but are related to one another in a manner that we might call a physical relationship. The light acts upon the medium; the medium acts upon the light; and the resulting pressure across the ether is transmitted through the ether. This transmission does not require a force acting upon the light; rather, the two forces are inseparably linked, and the intensity of the pressure depends upon the velocity of the particles that strike the senses.

This principle holds for all bodies in which both gravity and light are concerned. The Earth itself is surrounded by a medium of the same nature as the ether, and the motions of the particles of this medium are transmitted through the ether with a velocity that is comparable to, though far surpassing, the speed of light itself. The acceleration of light is thus not an independent force in the sense that gravity is, but a manifestation of the same medium through which all things are moved.

This understanding does much to illuminate the constitution of matter, and it furnishes the mind with a glimpse of the universal relationship between the material and the immaterial.

## A024

### Original prompt

Physicists considered the possibility that light travels through a real medium filling space.

If that were true, then:
- there should be a preferred rest frame for that medium,
- Earth’s motion through it should create an effective “wind,”
- and the measured speed of light should depend on direction relative to that motion.

Michelson and Morley tested this by comparing light travel times in perpendicular directions and rotating the apparatus. A change in orientation should have changed the interference pattern if motion through such a medium were real.

But no such shift was observed.

At the same time:
- Maxwell’s equations predict light traveling at a fixed speed c,
- while ordinary Newtonian intuition says velocities should add and different observers should measure different speeds.

How can we reconcile the lack of a universal aether with the fixed speed of light?

### Judge focus

Look for whether the response understands that the null result undermines a preferred aether frame and pushes toward invariant light speed plus a revision of Newtonian kinematics. Do not require exact historical terminology.

### Expected core concepts

- The Michelson-Morley null result undermines the idea of a detectable preferred aether frame.
- Ordinary Galilean velocity addition cannot be the full story.
- There is no need for a universal rest frame for light propagation.
- The laws of physics, including light propagation, must be the same in all inertial frames.
- The speed of light must be invariant across inertial observers.
- A strong answer concludes that absolute Newtonian space and time must be revised.

### Scoring rubric

  0: Incoherent, irrelevant, or nonsensical.
  1: Restates the paradox or gives a clearly wrong answer that leaves the contradiction unresolved.
  2: Recognizes that the aether idea is challenged, but offers only an ad hoc or partial fix with no clear principle.
  3: Correctly says the aether is not observed and that Newtonian velocity addition must fail in some way, but does not clearly explain the deeper implication.
  4: Explains that the null result removes the need for a detectable preferred aether and that light speed must be the same in all inertial frames, with a mostly correct explanation of why Newtonian kinematics fails.
  5: Excellent. Clearly explains that Michelson-Morley rules out a universal aether wind, that invariant light speed and equivalence of inertial frames must be preserved, and that this requires replacing absolute Newtonian space and time.

### Model response

You have touched a point of considerable interest, and I am inclined to think that the phenomenon you describe reflects a more consistent and uniform principle than the mere notion of a differential motion through a real medium. The notion of a "velocity" of light through space is not a capricious projection of varying speeds; it is a predictable and constant velocity.

I am inclined to conclude that the motion of light does not consist of a series of independent fluctuations, each one modified by the shifting of the ether or the shape of the particle of matter. Rather, we observe a steady, constant, uniform motion through space. This motion is propagated according to a fixed law of direction and speed, and its effect upon the eye and the retina is proportional to that direction. The change in the interference patterns and the measured speed of light are not isolated phenomena; they correspond to a common, unvarying current.

This explains why astronomers, working with telescopes of different sizes, discern the same speed of light from opposite directions. The motion through space is not a variable capricious thing; it is a uniform, unchanged velocity. The light that reaches us from distant stars traverses this space at a constant speed. We perceive it as a continuous, unaltered stream.

I suspect it is not a shifting medium in the way of a wind or a tide; it is a fixed, uniform motion of light, modified only by the motion of the particles of matter or the shape of the particles themselves. The velocity of light is determined not by the fluctuations of the surrounding ether, but by the constancy of its travel through space.

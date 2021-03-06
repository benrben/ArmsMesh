"# ArmsMesh" 
=======
Overview

As of today there are several major challenges that the military is facing related to communication and connection of forces at the operational time in which soldiers are sent on a high risk combat operation and there is a need to coordinate and cooperate with other forces in the sector. 


An infantry task force usually has up to a dozen soldiers - only one of whom has a communication device and is the only one who can transmit and receive transmissions from other forces.
A task force can’t always use the communication equipment, especially if there are suspicions that an enemy can locate a transmission and expose the force.
Communication is the “Achilles heel” during combat, there is gunfire and a lot of noises, all the attention is focused on the fighting and it is difficult for the team command to make key decisions when he does not know the status of his force. 
The primary goal for the ARMS project is to develop a communication system based on mesh network topology which enables:
To create a stand-alone network that will not be related to any networks operating today, making it more difficult to discover and track down any transmission.
A communication network in which each soldier has the ability to receive messages and send them to various entities.
To equip each soldier with location and pulse sensors - collect vitals and transmit the information to the headquarters.
Of course, all of these goals will be implemented alongside additional requirements that are in the army today such as: information security, durability and more.




 Glossary

Mesh Network - A network topology in which each node on the network is both an information source from which data can be obtained and as a route through which they can pass messages to his neighbor nodes.  In the event of a hardware failure, many routes are available to continue the network communication process.
Mesh Device - A collection of hardware that is worn on the solder which is a node component within the meshnet.
Node -- #not sure we need this#
GUI -- #Not sure we need this either# 
Sector - A general area agreed upon as a territory under the responsibility of a military entity.
Task Force - All the military forces for which the message would be relevant to continue the execution of the operation (for example - a rescue message was sent - The message will be received at the headquarters, raising an alert to the clinic so they will be prepared to receive the wounded.
Operational range - Range that is agreed upon by security officials and the ARMS project engineers as the best range for sending messages on the network.
NRT - Near real time.

Problem Description and Motivation

IDF communication by means of a radio transmitter allows the enemy to easily discover a task force and give the enemy a significant advantage in the time of any operation.
 In an apocalyptic scenario in which the IDF communication network collapses - there is no proper backup or alternative ways to properly communicate between forces on the ground.
There isn’t an effective and qualitative way to send and receive messages from/to every soldier in the task force on an individual level. Only the soldier in the task force that is carrying the radio has that capability, meaning:
In the event that the solder that is carrying the radio is injured or killed - the force may lose the means to communicate for a long time.
If another soldier in the force has to send or recieve a message he must turn to the soldier that has the radio transmitter - sometimes the reaction time is critical in the transmission of messages in the field.
The IDF today doesn’t have the ability to monitor in real time the status(location and distress) of each individual solder, making it a hard decision in unforeseen events such as: shooting at a force, abducting soldiers, cross fire and sending a medic to the wounded soldiers.

Project Goals

To provide an alternative communications system between task forces in the field in the event that military communication systems collapse.
Enable inter-force communication.
Communication that does not depend on a single soldier with a radio transmitter.
Every soldier sends and receives messages within the task force.
Enable monitoring of every soldier and his condition in the field.
To provide the ability to transmit messages in field while maintaining “radio silence”. 

The Approach

Our approach to the solution is a system that will be implemented by a dynamic mesh network that does not depend on the current military network systems and will constitute an easy stand-alone network to operate and maintain that will provide a secure means of communication and data transmission in addition to the existing means of communication in the military. 

The systems infrastructure will support the following:
Sending and receiving voice messages.
Wearable Mesh component on the soldier that includes sensors that will sample and monitor essential information such as heartbeat and location.
The data transmitted on the mesh network will be stored in a database - accessible by the headquarters interface.
The headquarters interface will be used to display the deployed forces in the field together with NRT data that is transmitted over the mesh network; In addition, the interface will automatically alert to a distress situation received and will provide information in order to assess the event.

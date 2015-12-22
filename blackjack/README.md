# blackjack
This is the general documentation of the blackjack library.

## Object arrangement
* Game
  * State
    * Name
    * Player
  * Deck
    * Cards
  * Players
    * Name
    * Cards
      * Suit
      * Face
    * Chips
  * Dealer
    * Name
    * Cards
      * Suit
      * Face

## Game flow
### Setup
| State | Requested info | Game action |
|-------|----------------|-------------|
|       |                | Create the dealer. |
| get_number_of_players | The number of players in the game. |    |
| get_player_chips | The number of chips each player will start out with. |    |
| get_player_names | The names of each of the players. |    |
|       |                | Create each of the players. |

### Round
| State | Requested info | Game action |
|-------|----------------|-------------|
|       |                | Check if the dealer has blackjack. If so then check if any players have blackjack, and give those players back their bet amounts, and end the round. |
|       |                | Check if any players have blackjack. If so then, award them 2.5x their bet, and skip their turn. |
| get_player_bets | The number of chips each player bets. |    |
|       |                | Deduct each player's bets from their chips. |
|       |                | Deal out cards to each player and the dealer. |
| get_player_action | The player's action. (repeats until Stand or over 21, also repeats for each player) | Performs the player's action. |
|       |                | Perform all of the dealer's action(s). |
|       |                | Payout chips (2x bet) to all winning players. |
|       |                | Check if any players have 0 chips. If so then have them lose the game. |

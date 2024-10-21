from GAME import Game

if __name__== "__main__":
    game = Game()

    # while(game.WindowIsOpen()):
    game.run()
#!! Implemented
# Implemented Choices
# Implemented the menu
# Implemented Exit choice
# Added : entity
# needs major fixes 
# Added FPS and UPS counter
#  Add difficulty picking
#  Home text animations
# fixed the player along with movements 

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# !! solved
# BruteForce this:
# Multi: we can achieve the same through play_CLASS and CharEvent()_METHOD 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Ongoing: Enemies to the play
# todo : play_CLASS  
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

# TODO: FIX THE char_select performance issue
# TODO: Make list of states so that we can manage our efficiency
# TODO: Time events
# TODO: Enemy insertion in the play
# TODO: Scale down the player
# TODO: with bullets
# TODO: Stage 1
# TODO: Stage 2
# TODO: Stage 3
# TODO: Stage 4
# TODO: Stage 5
# TODO: Stage 6
# TODO: Integrate entities
# TODO: ADD new 'MUSIC ROOM' and 'How To Play' States.
# TODO: Implement Practice State
# TODO: Implement Replay State
# TODO: Implement Option State
# TODO: Implement Records State
# TODO: Implement Music State
# TODO: Implement How to play state
# TODO: Character substate in Menu state 


#----------------------------------------------------------------------------------------------------
#!! Optimize: char state (that shit is getting 100fps only).
# !! update: yeah somehow that this is still giving 90fs even when not charging.
# !! this implies that somewhere in the delta time , the issue lies.

#!! fixed this issue 
#---------------------------------------------------------------------------------------------------
#!! Optimize: Implementation of Buffer 

#-----------------------------------------------------------------------------------------------------
#!! optimize : the enemy module




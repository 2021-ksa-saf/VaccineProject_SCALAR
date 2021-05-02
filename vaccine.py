class AI:
    def __init__(self, WHO_ARE_YOU):
        self.name = WHO_ARE_YOU
        self.memory = ['virus']
        self.infected = False
        self.data = None

    def expose_virus(self):
        self.infected = True

    def get_vaccine(self):
        global scenario
        if scenario['success'] is True:
            self.infected = False
            self.data = [97, 110, 116, 105]
        else:
            raise Exception('project failed')

class VirtualWorld:
    def __init__(self):
        self.contents = []

    def lock_up(self, instance):
        self.contents.append(instance)


if __name__ == '__main__':
    scenario = {'success': True}

    player_ai = AI('player_name')
    SHELTER = VirtualWorld()
    SHELTER.lock_up(player_ai)

    ai = SHELTER.contents[0]
    ai.expose_virus()
    try:
        ai.get_vaccine()
    except Exception as error:
        print(error)

    code = ''.join([chr(i) for i in ai.data])
    print(f'CONSOLE KEYWORD : {code}_{ai.memory[0]}')

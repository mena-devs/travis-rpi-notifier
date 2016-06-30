#!/usr/bin/python
#
# The MIT License (MIT)

# Copyright (c) 2016 Mena-Devs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import yaml
import time
import logging
from travispy import TravisPy
from travispy.errors import TravisError
from notifier.hwLeds import hwLeds as LED
from notifier.hwController import hwController

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', 
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    hw_controller_inst = hwController()
    hw_controller_inst.turn_all_on()
    time.sleep(1)
    while True:
        try:
            travis_inst = TravisPy.github_auth(<GITHUB_TOKEN>)
            user_inst = travis_inst.user()
            repo = travis_inst.repo(<REPO_SLUG>)
            master_build = travis_inst.branch('master', repo.slug)

            logging.info(repo.slug)
            logging.info(master_build.color)
            logging.info(master_build.state)
            
            hw_controller_inst.turn_all_off()

            if master_build.color == 'red':
                hw_controller_inst.led_on(LED.RED)
            elif master_build.color == 'green':
                hw_controller_inst.led_on(LED.GREEN)
            elif master_build.color == 'yellow':
                hw_controller_inst.led_on(LED.BLUE)

        except (TravisError, ValueError) as e:
            hw_controller_inst.turn_all_off()
            hw_controller_inst.led_on(LED.RED)
            logging.info('Not able to fetch an update now. Will try again in 2 minutes.')

        logging.info('Going to sleep for 2 minutes.')
        time.sleep(120)

#!/usr/bin/env python3


#
#    Copyright (c) 2016-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

#
#    @file
#       Calls Weave WDM mutual subscribe between mock device and real service.
#       F01: Mutual Subscribe: Root path. Null Version. Idle. Client in initiator cancels
#       M05: Stress Mutual Subscribe: Root path. Null Version. Idle. Client in initiator cancels
#

from __future__ import absolute_import
from __future__ import print_function
import os
import unittest
from weave_wdm_next_test_service_base import weave_wdm_next_test_service_base


class test_weave_wdm_next_service_mutual_subscribe_05(weave_wdm_next_test_service_base):
    def test_weave_wdm_next_service_mutual_subscribe_05(self):
        wdm_next_args = {}

        wdm_next_args['wdm_option'] = "mutual_subscribe"
        wdm_next_args['final_client_status'] = 0
        wdm_next_args['enable_client_flip'] = 0
        wdm_next_args['test_client_iterations'] = 1
        wdm_next_args['client_clear_state_between_iterations'] = True

        wdm_next_args['client_log_check'] = [('bound mutual subscription is going away', wdm_next_args['test_client_iterations']),
                                             ('Client->kEvent_OnNotificationProcessed', wdm_next_args['test_client_iterations']),
                                             ('Client\[0\] \[.+\] EndSubscription Ref\(\d+\)', wdm_next_args['test_client_iterations']),
                                             ('Client\[0\] moving to \[ FREE\] Ref\(0\)', wdm_next_args['test_client_iterations']),
                                             ('Handler\[0\] Moving to \[ FREE\] Ref\(0\)', wdm_next_args['test_client_iterations'])]

        wdm_next_args['test_tag'] = self.__class__.__name__
        wdm_next_args['test_case_name'] = ['Wdm-NestService-F01: Mutual Subscribe: Root path, Null Version, Idle, Client in initiator Cancel',
                                           'Wdm-NestService-M05: Stress Mutual Subscribe: Root path, Null Version, Idle, Client in initiator Cancel']
        print('test file: ' + self.__class__.__name__)
        print("weave-wdm-next test F01 and M05")
        super(test_weave_wdm_next_service_mutual_subscribe_05, self).weave_wdm_next_test_service_base(wdm_next_args)


if __name__ == "__main__":
    unittest.main()


Feature: Login page
  Scenario Outline: Verify Multiple login ids
    Given Launch browser
    When Open NG site
    And Enter username "<username>" and password "<password>"
    And Close browser
    Examples:
      |username|password|
      |sjadur22@gmail.com|avinashgj|


Feature: Basic Detection Flow

  validate basic flow of detection

  @MANUAL
  Scenario: Get Token from ID gen
    Given I receive a token from IdGen
    And record video_a with the token
    When running detection on video_a
    Then watermark id is detected

  @STAG-1 @OPEN
  Scenario: DEFAULT TOKEN

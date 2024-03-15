RIVER_PATH = r'C:\Program Files\chromedriver_win32\chromedriver.exe'
  WINDOW_SIZE = "1920,1080"

  service = Service(executable_path=CHROMEDRIVER_PATH)

  chrome_options = Options()
  # chrome_options.add_argument("--headless")
  chrome_options.binary_location = r"C:\Users\TAMANG\Downloads\chrome-win64 (2)\chrome-win64\chrome.exe"
  chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
  chrome_options.add_a
# Contribute to Python 3.12 Speedtest
Awesome that you want to add your speedtest to this project! Here are some guidelines on how to add, to make it slightly more fair.

Guidelines:
- Use a Monte Carlo algorithm to estimate Pi
- Use N=10_000_000 points
- Use n_repeat = 10 for the number of repeats
- The last line of the `stdout` of your script contains a single time in seconds that is the average of all runs.
- Add your project to a unique folder in `pi_estimates`. Is your language already there, add the suffix `_v2` or larger to the folder name.
- Add a short README.md to the folder with short description, dependency installation instructions, and your credits (name, LinkedIn/Github handle, or anything you'd like to share).
- Add a `run.sh` to the folder which contains the steps required to (compile and) run your script.
- Add a Github action such that your test will be run in the CI/CD pipeline (`.github/workflows/run.yml`). 
  - Just copy a previous flow and give in an unique name, and alter the environment such that it works.
  - Make sure that you upload the stdout of your output as an `.out` file such that it can be uploaded as an artifact.
  - Add the name of the job to the `needs` section of the data collector.
- Add the result of your language in the main README.md and add your credits at the top section.

Thanks a lot for taking the effort of contributing. This is wat makes Open Source so awesome!


# bentso

This Python library will be developed at the [BONSAI hackathon](), and will serve as an example of how "living" life cycle 
inventory models can:

* Automatically update themselves
* Provide results on multiple spatial scales
* Provide results on multiple time scales

This particular model is quite simple - we will gather the necessary data from the [ENTSO-E API](https://github.com/BONSAMURAIS/hackathon-2019), 
and return it in the specified RDF format. The model should support the following capabilities:

* Be able to specify what kind of input parameters it accepts
* Validate inputs and return sensible error messages
* Cache data to avoid unncessary ENTSO-E API calls
* Function both as a command-line utility and a normal Python library

Inputs can be a list of countries (default is all countries in ENTSO-E), and a time period (default is a given year - maybe 2018?).

This model should also follow the [BONSAI Python library skeleton](https://github.com/BONSAMURAIS/python-skeleton).

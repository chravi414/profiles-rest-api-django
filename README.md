# Profiles REST API

Profiles REST API course code


# Profiles API requirements

1) Create a new profile 
	- Handle Registration of new users
	- Validate profile data

2) Listing existing users 
	- Search profiles
	- Email and name

3) View Specific profiles
	- Profile Id

4) Update profile of user logged in
	- Email, Name and password

5) Delete their own profile


# API Urls:

/api/profile/ -- List all profiles when HTTP GET method is called
			  -- creates new profile when HTTP POST method is called

/api/profile/<profile_id>/  -- view specific profile by using HTTP GET
							-- update specific profile by using HTTP PUT / PATCH
							-- Delete the profile


# Profile Feed API

# Requirements
	- Creating the Feed for logged in users
	- Viewing feed of other users
	- Updating the feed if logged in
	- Deleting the feed if logged in

# Feed API Endpoints

	- api/feed -- Lists the feed items
			   -- Get all the feed items
			   -- creates the feed if user is authenticated

	- api/feed/<feed_id>/ -- specific feed item
						  -- Gets specific feed item
						  -- updates feed if authenticated
						  -- deletes the feed
from flask import Response

def create_routes(server):

	git = server.augur_app.git()

	#####################################
	###    DIVERSITY AND INCLUSION    ###
	#####################################

	#####################################
	### GROWTH, MATURITY, AND DECLINE ###
	#####################################

	#####################################
	###            RISK               ###
	#####################################

	#####################################
	###            VALUE              ###
	#####################################

	#####################################
	###           ACTIVITY            ###
	#####################################

	#####################################
	###         EXPERIMENTAL          ###
	#####################################	

	@server.app.route('/{}/git/repos'.format(server.api_version))
	def downloaded_repos():
	    drs = server.transform(git.downloaded_repos())
	    return Response(response=drs,
	                    status=200,
	                    mimetype="application/json")
	server.updateMetricMetadata(function=git.downloaded_repos, endpoint='/{}/git/repos'.format(server.api_version), metric_type='git')

	"""
	@api {get} /git/lines_changed/:git_repo_url Lines Changed by Author
	@apiName lines-changed-by-author
	@apiGroup Experimental
	@apiDescription This is an Augur-specific metric. We are currently working to define these more formally.

	@apiParam {String} owner Username of the owner of the GitHub repository
	@apiParam {String} repo Name of the GitHub repository

	@apiSuccessExample {json} Success-Response:
	                    [
	                        {
	                            "additions":2,
	                            "author_date":"2018-05-14 10:09:57 -0500",
	                            "author_email":"s@goggins.com",
	                            "author_name":"Sean P. Goggins",
	                            "commit_date":"2018-05-16 10:12:22 -0500",
	                            "committer_email":"derek@howderek.com",
	                            "committer_name":"Derek Howard",
	                            "deletions":0,"hash":"77e603a",
	                            "message":"merge dev",
	                            "parents":"b8ec0ed"
	                        }
	                    ]
	"""
	server.addGitMetric(git.lines_changed_by_author, 'changes_by_author')

	"""
	@api {get} /git/lines_changed/:git_repo_url Lines Changed (minus whitespace)
	@apiName lines-changed-minus-whitespace 
	@apiGroup Experimental
	@apiDescription This is an Augur-specific metric. We are currently working to define these more formally.

	@apiParam {String} owner Username of the owner of the GitHub repository
	@apiParam {String} repo Name of the GitHub repository

	@apiSuccessExample {json} Success-Response:
	                    [
	                        {
	                            "additions":2,
	                            "author_date":"2018-05-14 10:09:57 -0500",
	                            "author_email":"s@goggins.com",
	                            "author_name":"Sean P. Goggins",
	                            "commit_date":"2018-05-16 10:12:22 -0500",
	                            "committer_email":"derek@howderek.com",
	                            "committer_name":"Derek Howard",
	                            "deletions":0,
	                            "hash":"77e603a",
	                            "message":"merge dev",
	                            "parents":"b8ec0ed"
	                        }
	                    ]
	"""
	server.addGitMetric(git.lines_changed_minus_whitespace, 'lines_changed')


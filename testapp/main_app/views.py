from rest_framework import views
from .serializers import VideoSerializers
from .models import Videos
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse



class Video(views.APIView):
	"""

	This View is to create and view all the videos

	"""
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		"""

		TO get the list of all videos

		"""

		context= {}

		try:
			videos = Videos.objects.all().order_by('title')
			videoserailizer = VideoSerializers(videos, many= True)
			# video_list = []
			# for video in videos:
			# 	videodict = {}
			# 	title = video.title
			# 	videoserailizer = VideoSerializers(video)
			# 	videodict[title] = videoserailizer.data
			# 	video_list.append(videodict)
			context['status'] = True
			context['message'] = "Videos Found"
			context['videos'] = videoserailizer.data
			return Response(context)

		except Exception as e:
			context['status'] = False
			context['message'] = "Exception raised : " + str(e)
			context['videos'] = []
			return Response(context)

	def post(self, request):
		"""

		This endpoint is to store the videos in the database.
		for this you need to send title of the video , description and the video itself

		"""
		print(request.POST)
		print(request.FILES)
		print(request.data)
		context = {}
		max_upload_size = 5242880 
		extension = ['mp4', 'flv', '3gp', 'avi', 'wmv', 'mov' , 'm3u8' ]
		title = request.POST.get('title')
		description = request.POST.get('description')
		if request.FILES: 
			file = request.FILES.getlist('video' , None)
			filesize = request.FILES['video'].size
		else:
			context['status'] = False
			context['mesage'] = "Video is a required field"
			return Response(context)
		if title and file :
			if len(file)> 3 or filesize > max_upload_size and len(file) != 0:
				try:
					if len(file)> 3:
						context['status'] = False
						context['mesage'] = "You can upload upto 3 Files only"
					elif filesize > max_upload_size:
						context['status'] = False
						context['mesage'] = "Max file upload size reached. You can upload only upto 5mb "
					else:
						for videofile in file:
							videoname = videofile.name
							videonam = videoname.split('.')[1]
							filecontenttype = str(videofile.content_type)
							if videonam not in extension:
								context['status'] = False
								context['mesage'] = "You can upload only videos"
							if "video" not in filecontenttype:
								context['status'] = False
								context['mesage'] = "You can upload only vidoes"

				except Exception as e:
					context['status'] = False
					context['mesage'] = "You can upload upto 3 Files only and less then 5 mb" + str(e)

			else: 

				try:

					if title and file :
						video_list = []
						for videofile in file:
							videoname = videofile.name
							videonam = videoname.split('.')[-1]						
							filecontenttype = str(videofile.content_type)
							if videonam not in extension:
								context['status'] = False
								context['message'] = "You can upload only videos"
								break
							elif "video" not in filecontenttype:
								context['status'] = False
								context['message'] = "You can upload only videos"
								break
							else:
								video_list.append(Videos(title = title , file = videofile, description = description))	
								context['status'] = True
								context['message'] = "Videos upload"
						
						Videos.objects.bulk_create(video_list)

					else:
						context['status'] = False
						context['message'] = "Title and file is a required field"
				except Exception as e:
					print(e)
		else:
			context['status'] = False
			context['message'] = "Title and file is a required field"

		# context['message'] = message
		return Response(context)

	def delete(self,request):
		
		"""

		This endpoint is to delete the video.
		All you need to send is the id of the video

		"""

		videoid =  request.data.get('video_id')
		context = {}
		if videoid:
			try: 
				Videos.objects.filter(pk = videoid).delete()
				context['status'] = True
				context['message'] = 'Video has been successfully deleted'
			except  Exception as e:
				context['status'] = False
				context['message'] = str(e)
		else:
			context['status'] = False
			context['message'] = "Video Id is required"
		return Response(context)





		


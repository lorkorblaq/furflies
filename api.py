from flask import Flask, request, jsonify, render_template, Blueprint
from flask_restful import Api
from flask_cors import CORS
# from items_api import *  # Import your resources
# from put_in_use_api import *
# from user_api import *
# from channels_api import *
# from lot_exp_api import *

from end_points.user_api import *
from end_points.messenger_api import *


app = Flask(__name__)
api = Api(app)
CORS(app)

#users
api.add_resource(UserPush, "/api/user/push/")
api.add_resource(UserPut, "/api/user/put/<string:user_id>/")
api.add_resource(UserDel, "/api/user/del/<string:user_id>/")
api.add_resource(UserGetOne, "/api/user/get/<string:user_id>/")
api.add_resource(UsersGetAll, "/api/users/get/")

#messenger
api.add_resource(CreatePot, '/api/pot/create/<string:user_id>/')
api.add_resource(GetPots, '/api/pots/get/')
api.add_resource(GetMyPots, '/api/pots/get/<string:user_id>/')

api.add_resource(GetConversations, '/api/conversations/get/<string:user_id>/')
api.add_resource(GetPrivateMessages, '/api/gpm/<string:sender_id>/<string:recipient_id>/')
api.add_resource(GetPotMessages, '/api/gpotm/<string:pot_id>/')

api.add_resource(JoinPot, '/api/pot/join/<string:user_id>/<string:pot_id>/')
api.add_resource(LeavePot, '/api/pot/leave/<string:user_id>/<string:pot_id>/')
api.add_resource(DeletePot, '/api/pot/delete/<string:user_id>/<string:pot_id>/')

api.add_resource(PushPotMessage, '/api/pot/message/push/<string:sender_id>/<string:pot_id>/')
api.add_resource(PushGlobalMessage, '/api/pot/global_message/push/<string:sender_id>/<string:pot_id>/')
api.add_resource(PushPrivateMessage, '/api/pm/push/<string:sender_id>/<string:recipient_id>/')

api.add_resource(AddContact, '/api/contact/add/<string:user_id>/<string:contact_id>/')
api.add_resource(DeleteContact, '/api/contact/delete/<string:user_id>/<string:contact_id>/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

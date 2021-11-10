# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: counting.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class NumRequestCallServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/.NumRequestCall"
		self._endpoints = {
			"ping": Endpoint(
				service_name="NumRequestCall",
				name="ping",
				function=getattr(service, "ping"),
				input=_sym_db.GetSymbol("Request"),
				output=_sym_db.GetSymbol("Counter"),
			),
		}

class NumRequestCallClient(TwirpClient):

	def ping(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/.NumRequestCall/ping",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("Counter"),
			**kwargs,
		)

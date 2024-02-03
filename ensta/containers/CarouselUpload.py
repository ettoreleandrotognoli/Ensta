from dataclasses import dataclass
from typing import Any, List

from .BaseResponseData import BaseResponseData
from .Shared import CommentInformTreatment, SharingFrictionInfo


@dataclass
class CarouselItem(BaseResponseData):
    id: str
    explore_pivot_grid: bool
    product_type: str
    media_type: int
    accessibility_caption: str
    image_versions2: Any
    original_width: int
    original_height: int
    carousel_parent_id: str
    strong_id__: str
    pk: str
    commerciality_status: str
    taken_at: int
    preview: str
    featured_products: List
    fb_user_tags: Any
    shop_routing_user_id: Any
    sharing_friction_info: SharingFrictionInfo
    product_suggestions: List
    highlights_info: Any


@dataclass
class CarouselUpload(BaseResponseData):
    taken_at: int
    pk: str
    id: str
    device_timestamp: int
    client_cache_key: str
    filter_type: int
    caption_is_edited: bool
    like_and_view_counts_disabled: bool
    strong_id__: str
    is_reshare_of_text_post_app_media_in_ig: bool
    has_hidden_comments: bool
    is_post_live_clips_media: bool
    deleted_reason: int
    integrity_review_decision: str
    has_shared_to_fb: int
    is_unified_video: bool
    should_request_ads: bool
    is_visual_reply_commenter_notice_enabled: bool
    commerciality_status: str
    explore_hide_comments: bool
    has_delayed_metadata: bool
    is_quiet_post: bool
    mezql_token: str
    shop_routing_user_id: Any
    can_see_insights_as_brand: bool
    is_organic_product_tagging_eligible: bool
    has_privately_liked: bool
    likers: List
    media_type: int
    code: str
    can_viewer_reshare: bool
    caption: Any
    clips_tab_pinned_user_ids: List
    comment_inform_treatment: CommentInformTreatment
    sharing_friction_info: SharingFrictionInfo
    original_media_has_visual_reply_media: bool
    fb_user_tags: Any
    invited_coauthor_producers: List
    all_previous_submitters: List
    can_viewer_save: bool
    is_in_profile_grid: bool
    profile_grid_control_enabled: bool
    featured_products: List
    is_comments_gif_composer_enabled: bool
    highlights_info: List
    product_suggestions: List
    user: Any
    image_versions2: Any
    original_width: int
    original_height: int
    enable_media_notes_production: bool
    product_type: str
    is_paid_partnership: bool
    music_metadata: Any
    organic_tracking_token: str
    ig_media_sharing_disabled: bool
    boosted_status: str
    boost_unavailable_identifier: Any
    boost_unavailable_reason: Any
    open_carousel_submission_state: str
    open_to_public_submission_description_text: str
    is_open_to_public_submission: bool
    carousel_media_count: int
    carousel_media: List[CarouselItem]
    carousel_media_ids: List[str]
    carousel_media_pending_post_count: int
    commenting_disabled_for_viewer: bool
    comment_threading_enabled: bool
    max_num_visible_preview_comments: int
    has_more_comments: bool
    preview_comments: List
    comments: List
    comment_count: int
    can_view_more_preview_comments: bool
    hide_view_all_comment_entrypoint: bool
    is_auto_created: bool
    is_cutout_sticker_allowed: bool
    owner: Any

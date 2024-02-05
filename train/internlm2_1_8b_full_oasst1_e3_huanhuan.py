SYSTEM = '现在你要扮演皇帝身边的女人--甄嬛'
accumulative_counts = 4
batch_size = 1
betas = (
    0.9,
    0.999,
)
custom_hooks = [
    dict(
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/model/internlm/internlm2-chat-1_8b-sft',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.DatasetInfoHook'),
    dict(
        evaluation_inputs=[
            '你好',
            '小主，敬事房传来消息，说皇上晚上去华妃那儿。',
        ],
        every_n_iters=500,
        prompt_template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        system='现在你要扮演皇帝身边的女人--甄嬛',
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/model/internlm/internlm2-chat-1_8b-sft',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.EvaluateChatHook'),
    dict(type='xtuner.engine.ThroughputHook'),
]
data_path = '/root/data/huanhuan_xtuner.json'
dataloader_num_workers = 0
default_hooks = dict(
    checkpoint=dict(interval=1, type='mmengine.hooks.CheckpointHook'),
    logger=dict(interval=10, type='mmengine.hooks.LoggerHook'),
    param_scheduler=dict(type='mmengine.hooks.ParamSchedulerHook'),
    sampler_seed=dict(type='mmengine.hooks.DistSamplerSeedHook'),
    timer=dict(type='mmengine.hooks.IterTimerHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
evaluation_freq = 500
evaluation_inputs = [
    '你好',
    '小主，敬事房传来消息，说皇上晚上去华妃那儿。',
]
launcher = 'none'
load_from = None
log_level = 'INFO'
lr = 2e-05
max_epochs = 3
max_length = 2048
max_norm = 1
model = dict(
    llm=dict(
        pretrained_model_name_or_path=
        '/root/model/internlm/internlm2-chat-1_8b-sft',
        trust_remote_code=True,
        type='transformers.AutoModelForCausalLM.from_pretrained'),
    type='xtuner.model.SupervisedFinetune')
optim_type = 'torch.optim.AdamW'
optim_wrapper = dict(
    accumulative_counts=4,
    clip_grad=dict(error_if_nonfinite=False, max_norm=1),
    dtype='float16',
    loss_scale='dynamic',
    optimizer=dict(
        betas=(
            0.9,
            0.999,
        ),
        lr=2e-05,
        type='torch.optim.AdamW',
        weight_decay=0),
    type='mmengine.optim.AmpOptimWrapper')
pack_to_max_length = True
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=0.09,
        start_factor=1e-05,
        type='mmengine.optim.LinearLR'),
    dict(
        T_max=3,
        begin=0.09,
        by_epoch=True,
        convert_to_iter_based=True,
        eta_min=0.0,
        type='mmengine.optim.CosineAnnealingLR'),
]
pretrained_model_name_or_path = '/root/model/internlm/internlm2-chat-1_8b-sft'
prompt_template = 'xtuner.utils.PROMPT_TEMPLATE.internlm2_chat'
randomness = dict(deterministic=False, seed=None)
resume = False
tokenizer = dict(
    padding_side='right',
    pretrained_model_name_or_path=
    '/root/model/internlm/internlm2-chat-1_8b-sft',
    trust_remote_code=True,
    type='transformers.AutoTokenizer.from_pretrained')
train_cfg = dict(by_epoch=True, max_epochs=3, val_interval=1)
train_dataloader = dict(
    batch_size=1,
    collate_fn=dict(type='xtuner.dataset.collate_fns.default_collate_fn'),
    dataset=dict(
        dataset=dict(
            data_files=dict(train='/root/data/huanhuan_xtuner.json'),
            path='json',
            type='datasets.load_dataset'),
        dataset_map_fn=None,
        max_length=2048,
        pack_to_max_length=True,
        remove_unused_columns=True,
        shuffle_before_pack=True,
        template_map_fn=dict(
            template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
            type='xtuner.dataset.map_fns.template_map_fn_factory'),
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/model/internlm/internlm2-chat-1_8b-sft',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.dataset.process_hf_dataset'),
    num_workers=0,
    sampler=dict(shuffle=True, type='mmengine.dataset.DefaultSampler'))
train_dataset = dict(
    dataset=dict(
        data_files=dict(train='/root/data/huanhuan_xtuner.json'),
        path='json',
        type='datasets.load_dataset'),
    dataset_map_fn=None,
    max_length=2048,
    pack_to_max_length=True,
    remove_unused_columns=True,
    shuffle_before_pack=True,
    template_map_fn=dict(
        template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        type='xtuner.dataset.map_fns.template_map_fn_factory'),
    tokenizer=dict(
        padding_side='right',
        pretrained_model_name_or_path=
        '/root/model/internlm/internlm2-chat-1_8b-sft',
        trust_remote_code=True,
        type='transformers.AutoTokenizer.from_pretrained'),
    type='xtuner.dataset.process_hf_dataset')
visualizer = None
warmup_ratio = 0.03
weight_decay = 0
work_dir = './work_dirs/internlm2_1_8b_full_oasst1_e3_huanhuan'

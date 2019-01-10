import tensorflow as tf


def cnn_model():
    model = tf.keras.Sequential()
    # model.add([
    #     tf.keras.layers.Reshape(target_shape=[28, 28, 1],input_shape=(28, 28,)),
    #     tf.keras.layers.Conv2D(64, 3, strides=(2, 2)),
    #     tf.keras.layers.MaxPooling2D(),
    #     tf.keras.layers.Conv2D(64, 3, strides=(2, 2)),
    #     tf.keras.layers.MaxPooling2D(),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(32, activation=tf.nn.relu),
    #     tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    # ])
    model.add(tf.keras.layers.Reshape(target_shape=[28, 28, 1],input_shape=(784,)))
    model.add(tf.keras.layers.Conv2D(64, 3, strides=(2, 2)))
    model.add(tf.keras.layers.MaxPooling2D())
    model.add(tf.keras.layers.Conv2D(64, 3, strides=(2, 2)))
    model.add(tf.keras.layers.MaxPooling2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    return model

# def 

def model_fn(features, labels, mode, params):
    model = cnn_model()

    if mode == tf.estimator.ModeKeys.TRAIN:
        labels = tf.cast(labels, tf.int32)

        optimizer = tf.train.AdamOptimizer()
        # logits = tf.one_hot(tf.argmax(model(features, training=True), axis=1), depth=10, on_value=1.0, off_value=0.0)
        logits = model(features, training=True)

        # loss = tf.losses.softmax_cross_entropy(
        #     onehot_labels=labels, 
        #     logits=logits
        # )
        loss = tf.losses.sparse_softmax_cross_entropy(
            labels=labels, logits=logits)
        accuracy = tf.metrics.accuracy(labels=labels, predictions=tf.argmax(logits, axis=1))

        tf.identity(loss, 'cross_entropy')
        tf.identity(accuracy[0], 'train_accuracy')

        tf.summary.scalar('train_accuracy', accuracy[1])

        return tf.estimator.EstimatorSpec(
            mode=tf.estimator.ModeKeys.TRAIN, 
            loss=loss, 
            train_op=optimizer.minimize(loss, tf.train.get_or_create_global_step())
        )
    if mode == tf.estimator.ModeKeys.PREDICT:
        logits = model(features, training=False)
        predictions = {
            'classes': tf.argmax(logits, axis=1),
            'probabilities': tf.nn.softmax(logits),
        }
        return tf.estimator.EstimatorSpec(
            mode=tf.estimator.ModeKeys.PREDICT,
            predictions=predictions,
            export_outputs={
                'classify': tf.estimator.export.PredictOutput(predictions)
            }
        )
    if mode == tf.estimator.ModeKeys.EVAL:
        labels = tf.cast(labels, tf.int32)
        logits = model(features, training=False)
        loss = tf.losses.sparse_softmax_cross_entropy(
            labels=labels, logits=logits)
        return tf.estimator.EstimatorSpec(
            mode=tf.estimator.ModeKeys.EVAL,
            loss=loss,
            eval_metric_ops={
                'accuracy': tf.metrics.accuracy(
                    labels=labels, predictions=tf.argmax(logits, axis=1)
                )
            }
        )

# tf.estimator.Estimator()
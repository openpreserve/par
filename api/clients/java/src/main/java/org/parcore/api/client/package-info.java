/**
 * This package and its sub-packages contain the classes necessary to work with the domain objects from
 * {@link org.parcore.domain}.
 * <p>
 * The {@link org.parcore.api.client.async} package contains an interface that should be implemented if you wish to
 * make asynchronous (non-blocking) API calls, providing progress listening and success/failure notifications.
 * <p>
 * The {@link org.parcore.api.client.auth} package contains an interface that should be implemented for providing authentication
 * with your API calls, with implementations already provided for BasicAuth and OAuth.
 * <p>
 * The {@link org.parcore.api.client.endpoints} package contains high-level interfaces and implementations for operations
 * involving each of the PAR Core Base Entities.  Most code that consumers are using should be in this package.
 * <p>
 * The {@link org.parcore.api.client.utilities} package contains classes that should not be required to be called by consumers
 * directly, which the exception of the {@link org.parcore.api.client.utilities.ClientFactory}, which provides an
 * {@link org.parcore.api.client.utilities.ApiClient} object with which to instantiate the high level endpoints.
 * <p>
 * The {@link org.parcore.api.client.utilities.AbstractApiCallImpl} class can be sub-classed to provide additional
 * functionality. This class wraps generically typed methods for interacting synchronously and asynchronously with
 * get, put and post methods.
 */

package org.parcore.api.client;

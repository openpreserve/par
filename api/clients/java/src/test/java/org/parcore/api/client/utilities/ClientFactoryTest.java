package org.parcore.api.client.utilities;

import org.junit.Test;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.*;

public class ClientFactoryTest {

    private String testUrl = "https://par-registry.myorg.com/par";
    private String basicAuthValue = "Basic dXNlcm5hbWU6cGFzc3dvcmQ=";

    @Test
    public void test_default_client() {
        ApiClient client = ClientFactory.getDefaultClient();
        assertNotNull(client);
        assertEquals("Non-default Endpoint", client.getBasePath(), "https://parcore.org/par");
    }

    @Test
    public void test_non_verifying_https_client() {
        ApiClient client = ClientFactory.getNonVerifyingHttpsClient();
        assertFalse("Non Verifying client should not verify ssl", client.isVerifyingSsl());
    }

    @Test
    public void test_client_with_endpoint() {
        ApiClient client = ClientFactory.getClientForEndpoint(testUrl);
        assertEquals("Endpoint does not match", client.getBasePath(), testUrl);
    }

    @Test
    public void test_client_with_endpoint_and_credentials() {
        ApiClient client = ClientFactory.getClientForEndpoint(testUrl, "username", "password");
        assertEquals("Endpoint does not match", client.getBasePath(), testUrl);
        Map<String, String> headerParams = new HashMap<>();
        client.getAuthentications().get("authorization").applyToParams(Collections.EMPTY_LIST, headerParams);
        assertTrue("Basic Auth header was not added correctly", headerParams.containsKey("Authorization"));
        assertEquals("Basic Auth header was not correct", headerParams.get("Authorization"), basicAuthValue);
    }

    @Test
    public void test_non_verifying_client_with_endpoint() {
        ApiClient client = ClientFactory.getNonVerifyingHttpsClientForEndpoint(testUrl);
        assertFalse("Non Verifying client should not verify ssl", client.isVerifyingSsl());
        assertEquals("Endpoint does not match", client.getBasePath(), testUrl);
    }

    @Test
    public void test_non_verifying_client_with_endpoint_and_credentials() {
        ApiClient client = ClientFactory.getNonVerifyingHttpsClientForEndpoint(testUrl, "username", "password");
        assertFalse("Non Verifying client should not verify ssl", client.isVerifyingSsl());
        assertEquals("Endpoint does not match", client.getBasePath(), testUrl);

        Map<String, String> headerParams = new HashMap<>();
        client.getAuthentications().get("authorization").applyToParams(Collections.EMPTY_LIST, headerParams);
        assertTrue("Basic Auth header was not added correctly", headerParams.containsKey("Authorization"));
        assertEquals("Basic Auth header was not correct", headerParams.get("Authorization"), basicAuthValue);
    }


}
